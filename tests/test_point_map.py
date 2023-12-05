import pytest
from tasks.nearest_point import Point, PointMap


def test_add_point():
    point_map = PointMap()
    point = Point("1", 12, 6)
    point_map.add_point(point)
    assert point in point_map.points


def test_find_closest_point_insufficient_cities():
    point_map = PointMap()
    point = Point("1", 1, 1)
    with pytest.raises(ValueError):
        point_map.calculate_closest_point(point)


def test_find_closest_points():
    point_map = PointMap()
    point_1 = Point("1", 1, 1)
    point_2 = Point("2", 5, 5)
    point_3 = Point("3", 10, 10)
    point_4 = Point("4", 3, 3)

    point_map.add_point(point_1)
    point_map.add_point(point_2)
    point_map.add_point(point_3)
    point_map.add_point(point_4)

    closest_point = point_map.calculate_closest_point(point_1)
    assert closest_point == point_4
