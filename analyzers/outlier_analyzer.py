import pandas as pd

def outlier_analyzer(df):

    numeric_cols = [
        col for col in df.select_dtypes(
            include="number"
        ).columns
        if "Unnamed" not in col
    ]

    outlier_data = []

    for col in numeric_cols:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outlier_count = (
            (
                (df[col] < lower_bound)
                |
                (df[col] > upper_bound)
            )
        ).sum()

        outlier_data.append({
            "Column": col,
            "Outlier Count": outlier_count
        })

    outlier_df = pd.DataFrame(outlier_data)

    return outlier_df