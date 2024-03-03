import pytest



def test_distance():
    cases = [
        ((0.0,0.0),(0.0,1.0), 1.0),
        ((0.0,0.0),(1.0,0.0), 1.0),
        ((0.0,1.0),(0.0,1.0), 0),
        ((0.0,3.0),(4.0,0.0), 5.0),
    ]
    for ii, (start, finish, expected) in enumerate(cases):
        result =testee.distance(start, finish)
        assert result == pytest.approx(expected), f"test case {ii} failed"
