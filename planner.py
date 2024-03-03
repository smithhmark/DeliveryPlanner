import math
import sys


import shipment_file

DRIVER_COST = 500
DEPO = "DEPO"


def final_cost(drivers, total_distance):
    return DRIVER_COST * drivers + total_distance

def distance(start, finish):
    x1, y1 = start
    x2, y2 = finish
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

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

    distances = {}
    for dest, dpoint in destinations.items(): 
        distances[dest] = {}
        for origin, opoint in origins.items():
            dist = distance(dpoint, opoint)
            distances[dest][origin] = dist

    final_run_cost = {}
    for shipment in shipments:
        cost = distances[shipment][shipment] + distances[shipment][DEPO]

    return origins, destinations, distances, final_run_cost

def find_driver_route(distances, final_run_cost, allowed_shipments, max_duration=12*60):

    base_case = {}
    longest_duration = 0
    longest_route_starts_at = None
    longest_route_starting_at = {}
    longest_route_starting_at_contains = {}
    longest_route_starting_at_cost = {}
    longest_route_starting_at_fullcost = {}
    length_at = {}
    for shipment in allowed_shipments:
        route = [DEPO, shipment, DEPO]
        contains = set(route)
        cost = 0
        cost += distances[DEPO][shipment]
        cost += distances[shipment][shipment]
        fullcost = cost + distances[shipment][DEPO]

        if cost > longest_duration:
            longest_duration = fullcost
            longest_route_starts_at = shipment
        length_at[shipment] = 1
        longest_route_starting_at[shipment] = route
        longest_route_starting_at_contains[shipment] = contains
        longest_route_starting_at_cost[shipment] = cost
        longest_route_starting_at_fullcost[shipment] = fullcost

    added_a_shipment = True
    while added_a_shipment:
        added_a_shipment = False
        for shipment in allowed_shipments:
            # what shipment could we add to this route?
            cost_thru_shpmt = longest_route_starting_at_cost[shipment]
            total_shpmt_cost = longest_route_starting_at_fullcost[shipment]
            candidates = allowed_shipments - longest_route_starting_at_contains[shipment]
            best_candidate = None
            best_internal = 0
            best_full = float("inf")
            for candidate in candidates:
                internal_cost = distances[shipment][candidate] + distances[candidate][candidate]
                cfullcost = internal_cost + distances[candidate][DEPO]

                candidate_route_cost =  cfullcost + cost_thru_shpmt 
                if candidate_route_cost < max_duration:
                    if candidate_route_cost < best_full:
                        best_full = candidate_route_cost
                        best_candidate = candidate
                        best_internal = internal_cost
                        added_a_shipment = True
            if best_candidate is not None:
                longest_route_starting_at_fullcost[shipment] = candidate_route_cost
                longest_route_starting_at[shipment].append(best_candidate)
                longest_route_starting_at_cost[shipment] += best_internal
                longest_route_starting_at_contains[shipment].add(best_candidate)
                length_at[shipment] += 1
    
    almost_final = []
    for shipment in allowed_shipments:
        length = longest_route_starting_at_fullcost[shipment]
        route = longest_route_starting_at[shipment]
        almost_final.append((len(route), length, route))
    almost_final.sort(reverse=True)
    shipments_consumed, total_driving, shipments = almost_final[0]
    return shipments, total_driving


def cost_of_deliveries(shipments):
    origins, destinations, distances, final_run_cost = precalcs(shipments)
    allowed_shipments = set(shipments.keys())

    driver_routes = []
    total_length = 0
    while len(allowed_shipments) > 0:
        route, length = find_driver_route(distances, final_run_cost, allowed_shipments)
        driver_routes.append(route)
        allowed_shipments.difference_update(route)
        total_length += length
    return driver_routes

def main():
    path = sys.argv[1]
    shipments = shipment_file.load_file(path)

    routes = cost_of_deliveries(shipments)
    for route in routes:
        print(f"[{','.join(route)}]")

if __name__ == '__main__':
    main()
