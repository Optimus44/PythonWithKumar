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

def search_location(locations, location_id):
    """
    Searches for a location by its unique identifier within a list of locations.

    This function iterates through the provided list of locations and checks if the
    provided `location_id` matches the 'id' of any location in the list. If a match
    is found, it formats and returns the location details. If no match is found, it
    returns an appropriate message indicating that the location could not be found.

    :param location_id: The unique identifier of the location to be searched.
    :type location_id: str
    :param locations: A list of dictionaries containing location information. Each
        dictionary is expected to have the keys 'id', 'name', 'region', and
        'coordinates'.
    :type locations: list[dict]
    :return: A formatted string with the location details if found, or a message
        indicating that the location could not be found.
    :rtype: str
    """
    for location in locations:
        if location['id'] == location_id:
            print(f"ID: {location['id']}, "
                    f"Name: {location['name']}, "
                    f"Region: {location['region']}, "
                    f"Coordinates: {location['coordinates']}")
