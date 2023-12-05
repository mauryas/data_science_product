from tasks.nearest_point import Point


def test_point_positive_creation():
    """
    Test if a point of coordinates can be with positive integers.
    """
    point = Point("1", 1, 2)
    assert point.name == "1"
    assert point.x == 1
    assert point.y == 2


def test_point_negative_creation():
    """
    Test creation of negative points
    """
    point = Point("1", -1, -2)
    assert point.name == "1"
    assert point.x == -1
    assert point.y == -2
