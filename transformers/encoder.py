import pandas as pd

from sklearn.preprocessing import (
    LabelEncoder
)

def encode_features(
    df,
    columns,
    method
):

    working_df = df.copy()

    # Label Encoding
    if method == "label":

        encoder = LabelEncoder()

        for col in columns:

            working_df[col] = encoder.fit_transform(
                working_df[col].astype(str)
            )

    # One-Hot Encoding using getdummies function which performs onehot encoding
    elif method == "onehot":

        working_df = pd.get_dummies(
            working_df,
            columns=columns
        )

    return working_df