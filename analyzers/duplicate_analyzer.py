import pandas as pd

def duplicate_analyzer(df):

    duplicate_count = df.duplicated().sum()

    duplicate_df = pd.DataFrame({
        "Metric": ["Duplicate Rows"],
        "Count": [duplicate_count]
    })

    return duplicate_df