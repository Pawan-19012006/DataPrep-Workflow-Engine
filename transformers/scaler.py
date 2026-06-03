import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler

def scale_features(df,columns,method):
    working_df = df.copy()

    #Min Max Scaling
    if method == "minmax":
        scaler = MinMaxScaler()
    
    #Standard Scaling
    elif method == "standard":
        scaler = StandardScaler()

    #Apply Scaling
    working_df[columns] = scaler.fit_transform(
        working_df[columns]
    )

    return working_df