import pandas as pd

def remove_duplicates(df):
    working_df = df.copy()
    working_df = working_df.drop_duplicates()
    return working_df