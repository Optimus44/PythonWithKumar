def view_locations(a_list):
    """
    Prints location details for every element in the provided list of locations.

    The function iterates through a list containing location dictionaries and prints
    the details of each location, including its ID, name, region, and coordinates.

    :param a_list: A list of dictionaries, each representing a location.
        Each dictionary must contain the following keys: `id`, `name`, `region`,
        and `coordinates`.
    :type a_list: list[dict]
    :return: None
    """
    for location in a_list:
        print(f"ID: {location['id']}, "
              f"Name: {location['name']}, "
              f"Region: {location['region']}, "
              f"Coordinates: {location['coordinates']}")


# View only one location
def view_one_location(a_location):
    """
    Displays detailed information about a specific location.

    This function takes a dictionary representing a location and prints its
    details in a structured format, including its ID, name, region, and
    coordinates.

    :param a_location: Dictionary containing location data. It is expected to
        have the following keys: 'id', 'name', 'region', and 'coordinates'.
    :type a_location: dict

    :return: None
    """
    print(f"ID: {a_location['id']}, "
              f"Name: {a_location['name']}, "
              f"Region: {a_location['region']}, "
              f"Coordinates: {a_location['coordinates']}")


def search_location(locations, location_id):
    """
    Search for a location in a list of locations based on a given location ID.

    This function iterates through a list of location dictionaries and attempts
    to find the location that matches the specified location_id. If a match is
    found, the matching location dictionary is returned. If no match is found,
    the function returns None.

    :param locations: A list of dictionaries, where each dictionary represents
        a location and contains an 'id' key and other related location details.
    :type locations: list[dict]
    :param location_id: The identifier of the location to be searched.
    :type location_id: int or str
    :return: The dictionary of the matching location if found, or None if there's
        no match in the list of locations.
    :rtype: dict or None
    """
    for location in locations:
        if location['id'] == location_id:
            return location
    return None
