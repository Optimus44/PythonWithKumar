

def filter_by_region(locations, region):
    """
    Filters a list of locations based on a specified region. The function
    iterates through each location in the given list and checks if the
    location belongs to the specified region. If the region matches, the
    location is added to the resulting filtered list.

    :param locations: List of locations to filter. Each location should be
        a dictionary containing a 'region' field.
    :type locations: list[dict]
    :param region: The region used as a filter criterion.
    :type region: str
    :return: List of locations that match the specified region.
    :rtype: list[dict]
    """
    filtered_locations = []
    for location in locations:
        if location['region'] == region:
            filtered_locations.append(location)
    return filtered_locations