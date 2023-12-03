import math

import pandas as pd


from tasks.constants import DISTANCE_FILE_COLUMNS


class Point:
    """
    A class to represent a point.

    ...

    Attributes
    ----------
    name : str
        name of the point
    x : int
        x value of the point
    y : int
        y value of the point

    Methods
    -------
    print_point(): 
        Prints the points as Point(name, (x, y)).
    """

    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.x = x
        self.y = y

    def print_point(self):
        """print the point"""
        print(f"Point({self.name}, ({self.x}, {self.y}))")


class PointDistance:
    """
    A class to calculate distance between two points.

    ...

    Attributes
    ----------
    point_1 : Point
        first point
    point_1 : Point
        second point

    Methods
    -------
    calculate_euclidian_distance():
        calculate the euclidian distance between points
    """

    def __init__(self, point_1: Point, point_2: Point) -> None:
        self.point_1 = point_1
        self.point_2 = point_2

    def calculate_euclidian_distance(self) -> float:
        """
        method to calculate euclidian distance between two points.
        return:
            distance (float): distance between two points
        """
        distance = math.sqrt(
            ((self.point_2.x - self.point_1.x) ** 2)
            + ((self.point_2.y - self.point_1.y) ** 2)
        )
        return distance


class PointMap:
    """
    A class to store a list of points.

    ...

    Attributes
    ----------
    points : List[Point]
        list of points

    Methods
    -------
    add_point(point: Point):
        add a point to the points

    calculate_closest_point(point: Point):
        find the nearest point from the self.points 
        using euclidian distance.

    parse_dataframe(df: pd.DataFrame):
        parse a dataframe into list of points.

    """

    def __init__(self) -> None:
        self.points = []

    def add_point(self, point: Point) -> None:
        """
        add a point into the list of points.
        args:
            point: a variable of class point
        return:
            None
        """
        if not isinstance(point, Point):
            raise ValueError("Invalid point object. \
                             Please provide a Point instance.")

        self.points.append(point)

    def calculate_closest_point(self, point: Point) -> Point:
        """
        Calculte the closes point from the list of points.
        args:
            point (Point): the point for which we want to find 
                           the closes point.
        return:
            closest_point (Point): the closes point from the list.
        """
        if len(self.points) < 2:
            raise ValueError("Insufficient no. points to find closest point.")
        
        closest_point = {"point": None, "distance": math.inf}

        for point_2 in self.points:
            distance = PointDistance(point, point_2)\
                .calculate_euclidian_distance()
            if distance < closest_point["distance"]:
                if point.name != point_2.name:
                    closest_point = {"point": point_2, "distance": distance}

        return closest_point["point"]

    def parse_dataframe(self, df: pd.DataFrame) -> None:
        """
        Parse a dataframe into the Point and PointMap classes.
        args:
            df (pd.DataFrame): DataFrame of the list of points
        return:
            None
        """
        for row in df[DISTANCE_FILE_COLUMNS].itertuples():
            self.add_point(Point(name=row[1], x=row[2], y=row[3]))

    def print_points(self) -> None:
        """
        Print the points.
        """
        for point in self.points:
            point.print_point()
    
    def get_point_json(self) -> dict:
        points_json = []
        for point in self.points:
            points_json.append({
                'name': point.name,
                'x': point.x,
                'y': point.y
            })
        return points_json
