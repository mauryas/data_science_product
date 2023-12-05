import pandas as pd
from fastapi import APIRouter

from app.models import Accuracy
from data_science_product.tasks.constants import DECISION_TREE_TARGET
from data_science_product.tasks.decision_tree import DecisionTreeTrainer

router = APIRouter()


@router.get("/tree/train", response_model=Accuracy)
async def get_closest_point():
    """
    Train the decision tree model and send accuracy of the model.
    args:
        None
    return:
        (Accuracy)
    """
    df = pd.read_csv("data/raw_data/buy_computer.csv", dtype=str)

    decision_tree_trainer = DecisionTreeTrainer()

    X = decision_tree_trainer.preprocessing(df)
    y = df[DECISION_TREE_TARGET]

    # Train decision tree with cross-validation
    accuracy = decision_tree_trainer.train_with_cross_validation(X, y)

    return {"accuracy": round(accuracy, 4)}
