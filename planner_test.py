import pytest

import planner as testee

@pytest.fixture
def origins():
    return {
        "DEPO": (0.0, 0.0),
        "1": (-9.100071078494038,-48.89301103772511),
        "2": (73.38933871575719,-86.93443314676254),
        "3": (-109.23071648186891,-94.63347501104835),
        "4": (-126.02559605503424,12.036481800074222),
        "5": (-113.02298711580897,-28.788384418439914),
        "6": (-138.81585973557097,-7.31025663667895),
        "7": (86.85115717568146,89.48744886950469),
        "8": (-66.54751655340681,-44.928590189503765),
        "9": (-41.48405901129298,-139.38690997500595),
        "10": (-81.03383480274111,-15.260530169659576),
    }

@pytest.fixture
def destinations():
    return {
        "DEPO": (0.0, 0.0),
        "1": (-116.78442279683607,76.80147820713637),
        "2": (-57.594533352956425,28.662926099543245),
        "3": (134.9870047348522,-41.02728921942559),
        "4": (-102.90992982127393,-41.30183670469724),
        "5": (-5.185068924995978,-89.13459423667982),
        "6": (114.91425212820523,43.59244241133117),
        "7": (-17.298239574244576,33.53842243361643),
        "8": (-7.970268610868698,-44.13604272102903),
        "9": (-82.99128121032932,73.38972329128366),
        "10": (85.97373147108725,-46.40031412793837),
    }


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

def test_precalc_distances(origins, destinations):
    distances = testee.precalc_distances(origins, destinations)
    DEPO="DEPO"
    #print(distances)
    for load_id in range(1,11):
        load_id = str(load_id)
        d1 = testee.distance(origins[load_id], destinations[load_id])
        d2 = distances[load_id][load_id]
        assert d1 == d2,f"{load_id} distance wrong"

        d1 = testee.distance((0.0,0.0), origins[load_id])
        print(d1)
        d2 = distances[DEPO][load_id]
        assert d1 == d2, f"{load_id} Origin distance distance from DEPO wrong"

        d1 = testee.distance(destinations[load_id], (0.0,0.0))
        d2 = distances[load_id][DEPO]
        assert d1 == d2,f"{load_id} dest distance to DEPO wrong"

    for load1_id, load2_id in zip( range(1,11), range(2,11)):
        load1_id = str(load1_id)
        load2_id = str(load2_id)

        d1 = testee.distance(destinations[load1_id], origins[load2_id])
        d2 = distances[load1_id][load2_id]
        assert d1 == d2, f"{load1_id}->{load2_id} distance wrong"


