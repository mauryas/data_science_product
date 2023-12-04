import pandas as pd
from pandas import DataFrame

from sklearn.model_selection import cross_val_score, KFold
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import OrdinalEncoder


class FeatureEnginerring:
    """
    A class to do feature engineering.

    ...

    Attributes
    ----------
    ordinal_encoder : OrdinalEncoder
        ordinal encoder

    Methods
    -------
    transform_ordinal(df: DataFrame):
        transform ordinal features

    transform_one_hot(df: DataFrame):
        transform feature to one hot encode

    """

    def __init__(self):
        self.ordinal_encoder = OrdinalEncoder()

    def transform_ordinal(self, df: DataFrame) -> DataFrame:
        """
        Transform the age, income and credit rating based low to high.
        args:
            df (DataFrame): input data frame
        return:
            df_encoded (DataFrame): ordinal encoded dataframe
        """
        ordinal_features = ["age", "income", "creditRating"]
        level_age = ["<=30", "30-40", ">40"]
        level_income = ["low", "medium", "high"]
        level_credit_rating = ["fair", "excellent"]

        self.ordinal_encoder = OrdinalEncoder(
            categories=[level_age, level_income, level_credit_rating]
        )
        self.ordinal_encoder.fit(df[ordinal_features])

        enc_array = self.ordinal_encoder.transform(df[ordinal_features])
        df_transformed = DataFrame(enc_array, columns=ordinal_features)

        return df_transformed

    def transform_one_hot(self, df: DataFrame) -> DataFrame:
        """
        One hot encode student
        args:
            df (DataFrame): input data frame
        return:
            df_encoded (DataFrame): one hot encoded dataframe
        """

        df_transformed = pd.get_dummies(df["student"], dtype=float)

        return df_transformed


class DecisionTreeTrainer:
    """
    A class to do feature engineering.

    ...

    Attributes
    ----------
    n_folds : int
        number of folds
    clf: DecisionTreeClassifier
        decision tree model
    kf: KFold
        generate k folds

    Methods
    -------
    train_with_cross_validation(X: DataFrame, y: DataFrame):
        cross validation

    inverse_transform_ordinal(df: DataFrame):
        inverse transform ordinal features

    transform_one_hot(df: DataFrame):
        transform feature to one hot encode

    inverse_transform_one_hot(df: DataFrame):
        inverse transform feature from one hot encode

    """

    def __init__(self, n_folds=5):
        self.n_folds = n_folds
        self.clf = DecisionTreeClassifier()
        self.kf = KFold(n_splits=n_folds, shuffle=True, random_state=42)

    def train_with_cross_validation(self, X: DataFrame, y: DataFrame) -> float:
        """
            Train decision tree using n-fold cross-validation.
            and print accuracies.
            args:
                X (DataFrame) - feature set
                y (DataFrame) - target
        """
        fold_accuracies = cross_val_score(self.clf, X, y, cv=self.kf)

        return fold_accuracies.mean()

    def print_rules(self, X: DataFrame, y: DataFrame) -> None:
        """
            Print decision tree rules.
            args:
                X (DataFrame) - feature set
                y (DataFrame) - target
        """
        self.clf.fit(X, y)
        tree_rules = export_text(self.clf, feature_names=list(X.columns))
        print("Decision Tree Rules:")
        print(tree_rules)

    def preprocessing(self, df: DataFrame) -> DataFrame:
        """
        Convert age, income and credit score into ordinal and
        student as one hot.
        args:
            df (DataFrame): dataset
        return:
            df_feature (DataFrame): processed features
        """
        fe = FeatureEnginerring()

        df_ord = fe.transform_ordinal(df)
        df_one_hot = fe.transform_one_hot(df)

        df_feature = pd.concat([df_ord, df_one_hot], axis=1)

        return df_feature
