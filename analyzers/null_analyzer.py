import pandas as pd

def null_analyzer(df):

    null_counts = df.isnull().sum()

    df_null_vals = pd.DataFrame({
        "Column": null_counts.index,
        "Null Values": null_counts.values
    })

    return df_null_vals