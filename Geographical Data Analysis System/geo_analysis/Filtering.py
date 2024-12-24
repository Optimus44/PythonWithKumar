def old_filter_by_region(locations, region):
    """
    Filters and prints location details based on the specified region. If no locations in the given
    region are found, a message indicating this is printed. Each matching location's ID, name, region,
    and coordinates are displayed.

    :param locations: List of location dictionaries, where each dictionary contains details about a
        location, including its region, ID, name, and coordinates.
    :type locations: list[dict]
    :param region: The region by which the locations list should be filtered.
    :type region: str
    :return: None
    """
    found = False
    for location in locations:
        if location['region'] == region:
            print(f'ID: {location["id"]}, Name: {location["name"]}, Region: {location["region"]}, Coordinates: {location["coordinates"]}')
            found = True

    # If we want to write better codes, we can return a list of locations that can be view using the view_locations() function. Think about.
    if not found:
        print("No locations found in this region.")


def filter_by_region(locations, region):
    found = False
    filtered_locations = []
    for location in locations:
        if location['region'] == region:
            filtered_locations.append(location)
            found = True

    if not found:
        print("No locations found in this region.")

    return filtered_locations