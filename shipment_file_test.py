import pytest

import shipment_file as testee

@pytest.fixture
def shipment_name():
    return "1"

@pytest.fixture
def shipment_origin():
    return "-9.100071078494038", "-48.89301103772511"

@pytest.fixture
def shipment_destination():
    return "-116.78442279683607", "76.80147820713637"

@pytest.fixture
def example_shipment_line(shipment_name, shipment_origin, shipment_destination):
    return f"{shipment_name} ({shipment_origin[0]},{shipment_origin[1]}) ({shipment_destination[0]},{shipment_destination[1]})"

@pytest.fixture
def example_file_contents():
    return """loadNumber pickup dropoff
1 (-9.100071078494038,-48.89301103772511) (-116.78442279683607,76.80147820713637)
2 (73.38933871575719,-86.93443314676254) (-57.594533352956425,28.662926099543245)
"""

@pytest.fixture
def example_file_lines(example_file_contents):
    return example_file_contents.lines()


def test_parse_line(example_shipment_line, shipment_name, shipment_origin, shipment_destination):
    rcvd = testee.parse_line(example_shipment_line)

    assert len(rcvd) == 3
    name, origin, dest = rcvd  

    assert name == shipment_name, "parsed incorrect shipment name"
    assert origin == shipment_origin, "parsed incorrect shipment origin"
    assert dest == shipment_destination, "parsed incorrect shipment destination"

