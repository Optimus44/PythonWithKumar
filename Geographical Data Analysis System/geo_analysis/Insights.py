from .DistanceCalculation import calculate_distance


def total_regions(locations):
    """
    Analyzes a list of location dictionaries and calculates the total count
    of each region specified in the input list. The regions counted include
    'Eastern', 'Western', 'Northern', 'Southern', and 'Central'. The function
    outputs the counts for each region but does not return any value.

    :param locations: A list of dictionaries where each dictionary contains
                      a 'region' key indicating the region to which a location
                      belongs ('Eastern', 'Western', 'Northern', 'Southern',
                      or 'Central').
    :type locations: list[dict]

    :return: None
    """

    east_locations = 0
    west_locations = 0
    north_locations = 0
    south_locations = 0
    central_locations = 0

    for location in locations:
        if location['region'] == 'Eastern':
            east_locations += 1
        elif location['region'] == 'Western':
            west_locations += 1
        elif location['region'] == 'Northern':
            north_locations += 1
        elif location['region'] == 'Southern':
            south_locations += 1
        else:
            central_locations += 1

    # These should be displayed depending on user input

    location_input = input('Enter location: ')
    if location_input == 'Eastern':
        print('East: ', east_locations)
    elif location_input == 'Western':
        print('West: ', west_locations)
    elif location_input == 'Northern':
        print('North: ', north_locations)
    elif location_input == 'Southern':
        print('South: ', south_locations)
    elif location_input == 'Central':
        print('Central: ', central_locations)
    else:
        print('Invalid location')


def total_regionss(region):
    pass

def furthest_distance(list_of_locations):
    i = 0
    farthest_distance = 0
    for point_a in list_of_locations:
        i += 1
        for point_b in list_of_locations[i:]:
            distance = calculate_distance(point_a['coordinates'], point_b['coordinates'])
            if distance > farthest_distance:
                farthest_distance = distance

    return farthest_distance


def try_this():
    pass
