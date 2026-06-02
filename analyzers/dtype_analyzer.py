import pandas as pd

def analyze_dtypes(df):
    dtype_df = pd.DataFrame({
        "Column" : df.columns,
        "Datatype" : df.dtypes.values
    })

    return dtype_df