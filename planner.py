

def parse_location_tuple(loc_str):
    # "(<x>,<y>)"
    bits = loc_str.split(',')
    assert len(bits) == 2, "too many components to location string"

    x_str = bits[0][1:]
    y_str = bits[1][:-1]
    return x_str, y_str


def parse_line(line):
    bits = line.split()
    delivery_name = bits[0]
    delivery_origin = parse_location_tuple(bits[1])
    delivery_destination = parse_location_tuple(bits[2])
    return delivery_name, delivery_origin, delivery_destination


def parse_shipments(lines):
    shipments = {}
    for line in lines[1:]:
       delivery_name, delivery_origin, delivery_destination = parse_line(line)

        shipments[delivery_name] = (delivery_origin, delivery_destination)
    return shipments
       

def load_file(file_name):
    with open(file_name, r'r') as fil:
        shipments = parse_shipments(fil.readlines())
    return shipments


