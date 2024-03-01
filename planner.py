import math

DRIVER_COST = 500

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

def final_cost(drivers, total_distance):
    return DRIVER_COST * drivers + total_distance

def distance(start, finish):
    x1, y1 = start
    x2, y2 = finish
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def precalcs(shipments):
    raw_origins = [("0", "0.0","0.0")]
    raw_destinations = [("0", "0.0","0.0")]

    for shpname, (origin, dest) in shipments.items():
        raw_origins.append(shpname, origin[0], origin[1])
        raw_destinations.append(shpname, dest[0], dest[1])

    origins = {}
    for name, x_str, y_str in raw_origins:
        x = float(x_str)
        y = float(y_str)
        origins[name] = (x,y)

    distinations = {}
    for name, x_str, y_str in raw_origins:
        x = float(x_str)
        y = float(y_str)
        distinations[name] = (x,y)

    for origin, opoint in origins.items():
        for dest, dpoint in destinations.items(): 
            pass

    distances = {}
    return None

def cost_of_days_deliveries(shipments):
    pass


