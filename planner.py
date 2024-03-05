import math
import sys

import shipment_file
import cli

DRIVER_COST = 500
DEPO = "DEPO"


def final_cost(drivers, total_distance):
    return DRIVER_COST * drivers + total_distance


def distance(start, finish):
    x1, y1 = start
    x2, y2 = finish
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def total_cost(num_drivers, total_distance_traveled):
    return DRIVER_COST*num_drivers + total_distance_traveled


def precalc_distances(origins, destinations):
    distances = {}
    for dest, dpoint in destinations.items(): 
        distances[dest] = {}
        for origin, opoint in origins.items():
            dist = distance(dpoint, opoint)
            distances[dest][origin] = dist
    return distances


def precalcs(shipments):
    raw_origins = [(DEPO, "0.0","0.0")]
    raw_destinations = [(DEPO, "0.0","0.0")]

    for shpname, (origin, dest) in shipments.items():
        raw_origins.append((shpname, origin[0], origin[1]))
        raw_destinations.append((shpname, dest[0], dest[1]))

    origins = {}
    for name, x_str, y_str in raw_origins:
        x = float(x_str)
        y = float(y_str)
        origins[name] = (x,y)

    destinations = {}
    for name, x_str, y_str in raw_origins:
        x = float(x_str)
        y = float(y_str)
        destinations[name] = (x,y)

    distances = precalc_distances(origins, destinations)

    final_run_cost = {}
    for shipment in shipments:
        cost = distances[shipment][shipment] + distances[shipment][DEPO]

    return origins, destinations, distances, final_run_cost


def find_driver_route(distances, final_run_cost,
                      allowed_shipments, max_duration=12*60):
    base_case = {}
    longest_route = {}
    longest_route_starting_at_contains = {}
    longest_route_all_but_return = {}
    longest_route_round_trip = {}
    shipments_per_route = {}

    # setup singleton shipments for each possible starting point
    for shipment in allowed_shipments:
        route = [shipment]
        contains = set(route)
        required_dist = 0
        required_dist += distances[DEPO][shipment] # dist to origin
        required_dist += distances[shipment][shipment] # dist to dest
        round_trip_distance = required_dist + distances[shipment][DEPO]

        shipments_per_route[shipment] = 1
        longest_route[shipment] = route
        longest_route_starting_at_contains[shipment] = contains
        longest_route_all_but_return[shipment] = required_dist
        longest_route_round_trip[shipment] = round_trip_distance

    added_a_shipment = True
    while added_a_shipment:
        added_a_shipment = False
        for shipment in allowed_shipments:
            # what shipment could we add to this route?
            dist_to_now = longest_route_all_but_return[shipment]
            route_round_trip_dist = longest_route_round_trip[shipment]

            assert route_round_trip_dist < max_duration, f"wehave gone too far: {shipment}, {longest_route[shipment]}, {route_round_trip_dist} >= {max_duration}"
            """
            """

            candidates = allowed_shipments - longest_route_starting_at_contains[shipment]
            best_candidate = None
            best_internal = float("inf")
            best_candidate_round_trip = float("inf")
            for candidate in candidates:
                internal_cost = distances[shipment][candidate] + distances[candidate][candidate]
                final_shipmt_dist = internal_cost + distances[candidate][DEPO]

                candidate_route_cost =  dist_to_now + final_shipmt_dist
                candidate_internal =  internal_cost + dist_to_now
                if candidate_route_cost >= max_duration:
                    continue
                if candidate_route_cost < max_duration:
                    if candidate_route_cost < best_candidate_round_trip and candidate_internal < best_internal:
                        best_candidate_round_trip = candidate_route_cost
                        best_candidate = candidate
                        best_internal = internal_cost
                        added_a_shipment = True

            """
            if best_candidate_round_trip != float("inf"):
                assert best_candidate_round_trip < max_duration, f"toofar: {shipment}, {longest_route[shipment]}, {best_candidate_round_trip}"
            """
            if best_candidate is not None:
                longest_route_round_trip[shipment] = best_candidate_round_trip
                longest_route[shipment].append(best_candidate)
                longest_route_all_but_return[shipment] = best_internal
                longest_route_starting_at_contains[shipment].add(best_candidate)
                shipments_per_route[shipment] += 1
    
    almost_final = []
    for shipment in allowed_shipments:
        round_trip_dist = longest_route_round_trip[shipment]
        route = longest_route[shipment]
        almost_final.append((len(route), round_trip_dist, route))
    almost_final.sort(reverse=True)
    shipments_consumed, total_driving, shipments = almost_final[0]
    return shipments, total_driving


def cost_of_deliveries(shipments, verbose=False):
    origins, destinations, distances, final_run_cost = precalcs(shipments)
    allowed_shipments = set(shipments.keys())

    driver_routes = []
    total_length = 0
    rt_lengths = [] 
    while len(allowed_shipments) > 0:
        route, length = find_driver_route(distances, final_run_cost, allowed_shipments)
        driver_routes.append(route)
        allowed_shipments.difference_update(route)
        total_length += length
        rt_lengths.append(length)

    if verbose:
        total = total_cost(len(driver_routes), total_length)
        print(f"Total cost:{total}")
        print("Driver-Route Breakdown:")
        print("\tdriver\tlength of route")
        for ii, length in enumerate(rt_lengths):
            print(f"\t{ii}\t{length}")

    return driver_routes


def main():
    args = cli.parse_args()

    shipments = shipment_file.load_file(args.shipment_file)

    routes = cost_of_deliveries(shipments, args.is_verbose)
    for route in routes:
        print(f"[{','.join(route)}]")


if __name__ == '__main__':
    main()
