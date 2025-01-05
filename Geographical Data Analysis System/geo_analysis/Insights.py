from .DistanceCalculation import calculate_distance


def furthest_distance(list_of_locations):
    """
    Calculate the furthest distance between two locations in a list.

    This function computes the maximum distance between any two locations
    from the given list of locations. Each location is represented as a
    dictionary and must contain 'coordinates' in its data structure. It uses
    `calculate_distance` to compute the distance between two points. The
    function iterates through the list of locations in pairs, comparing
    distances, and returns the maximum distance found alongside the two
    location dictionaries corresponding to this distance.

    :param list_of_locations: A list of dictionaries where each dictionary
        must contain a key 'coordinates', which represents the coordinates
        of the given location.
    :type list_of_locations: list[dict]

    :return: A tuple containing:
        - (float) The farthest distance calculated.
        - (dict) The first location dictionary of the farthest pair.
        - (dict) The second location dictionary of the farthest pair.
    :rtype: tuple[float, dict, dict]
    """
    # This should receive a filtered location_list
    i = 0
    farthest_distance = 0
    for point_a in list_of_locations:
        i += 1
        for point_b in list_of_locations[i:]:
            distance = calculate_distance(point_a['coordinates'], point_b['coordinates'])
            if distance > farthest_distance:
                farthest_distance = distance
                location_1 = point_a
                location_2 = point_b

    return farthest_distance, location_1, location_2

