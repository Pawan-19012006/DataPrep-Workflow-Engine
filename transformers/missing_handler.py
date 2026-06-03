import pandas as pd

def handle_missing_values(df,columns,method):
    working_df = df.copy()

    #Mean Imputation
    if method == "mean":
        for col in columns:
            working_df[col] = working_df[col].fillna(
                working_df[col].mean()
            )
    
    #Median imputation
    elif method == "median":
        for col in columns:
            working_df[col] = working_df[col].fillna(
                working_df[col].median()
            )
    
    #Mode imputation
    elif method == "mode":
        for col in columns:
            working_df[col] = working_df[col].fillna(
                working_df[col].mode()[0]
            )

    #Row Deletion
    elif method == "drop_rows":
        working_df = working_df.dropna(
            subset=columns
        )

    return working_df

