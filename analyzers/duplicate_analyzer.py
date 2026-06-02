import pandas as pd

def duplicate_analyzer(df):

    duplicate_counts = df.apply(lambda col: col.duplicated().sum())
    df_dupes = pd.DataFrame({
        "Columns" : duplicate_counts.index,
        "Duplicates" : duplicate_counts.values
    })
    return df_dupes