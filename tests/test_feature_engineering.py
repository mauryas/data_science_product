import pandas as pd
from pandas.testing import assert_frame_equal

from tasks.decision_tree import FeatureEnginerring


def test_transform_ordinal():
    """
    Test the transform ordinal is working correctly.
    """
    df = pd.DataFrame({'age': ["<=30", "30-40", ">40"], 
                       'income': ["low", "medium", "high"],
                       'creditRating': ["fair", "excellent", "fair"]
                    })
    df_transform_expected = pd.DataFrame({'age': [0.0, 1.0, 2.0], 
                       'income': [0.0, 1.0 , 2.0],
                       'creditRating': [0.0, 1.0, 0.0]
                    })
    fe = FeatureEnginerring()
    df_transform = fe.transform_ordinal(df)
    assert assert_frame_equal(df_transform, df_transform_expected, check_dtype=False) is None

def test_transform_one_hot():
    """
    Test the transform ordinal is working correctly.
    """
    df = pd.DataFrame({
        'student': ["yes", "no"],                
                    })
    df_transform_expected = pd.DataFrame({
                                          'no': [0.0, 1.0],
                                          'yes': [1.0, 0.0]
                                          })
    fe = FeatureEnginerring()
    df_transform = fe.transform_one_hot(df)
    assert assert_frame_equal(df_transform, df_transform_expected, check_dtype=False) is None

