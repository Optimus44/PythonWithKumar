def calculate_distance(point_a, point_b):
    """
    Calculates the distance in kilometers between two points on a 2D plane.

    This function computes the distance between two points represented by their
    coordinates on a 2D Cartesian plane. The result is adjusted by a constant
    multiplier (111) to approximate the distance in kilometers.

    :param point_a: A tuple containing the x and y coordinates of the first point.
    :param point_b: A tuple containing the x and y coordinates of the second point.
    :return: The calculated distance in kilometers as a float.
    """
    return (((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2 ) ** 0.5) * 111