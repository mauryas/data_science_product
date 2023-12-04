import pandas as pd
from fastapi import APIRouter

from app.models import PointMapResponse, PointResponse
from tasks.nearest_point import PointMap

router = APIRouter()


@router.get("/points", response_model=PointMapResponse)
async def get_points():
    """
    return all the points available
    args:
        None
    return:
        points_obj (PointMapResponse) all point available
    """
    df = pd.read_csv("data/raw_data/sample_distance.csv")

    points_obj = PointMap()
    points_obj.parse_dataframe(df)

    points_json = points_obj.get_point_json()

    return {"points": points_json}


@router.post("/points/closest", response_model=PointResponse)
async def post_closest_point(
    point: PointResponse = PointResponse(name="City 2", x=17, y=11)
):
    """
    get the closes point from the provided points.
    args:
        point (PointResponse) - point to find the closest
    return:
        closest_point (PointResponse) the closes point to the provided
    """
    df = pd.read_csv("data/raw_data/sample_distance.csv")

    points_obj = PointMap()
    points_obj.parse_dataframe(df)
    closest_point = points_obj.calculate_closest_point(point)

    return closest_point
