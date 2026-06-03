import pandas as pd

def remove_outliers_iqr(
        df,
        columns
):
    working_df = df.copy()
    for col in columns:
        Q1 = working_df[col].quantile(0.25)
        Q3 = working_df[col].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        working_df = working_df[
            (working_df[col]>=lower_bound)
            &
            (working_df[col]<= upper_bound)
        ]

    return working_df