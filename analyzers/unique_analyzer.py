import pandas as pd

def unique_analyzer(df):

    unique_data = []

    for column in df.columns:

        unique_count = df[column].nunique()

        unique_percentage = (
            unique_count / len(df)
        ) * 100

        sample_values = (
            df[column]
            .dropna()
            .unique()[:5]
        )

        # Cardinality Classification
        if unique_count <= 10:

            cardinality = "Low"

        elif unique_count <= 50:

            cardinality = "Medium"

        else:

            cardinality = "High"

        unique_data.append({

            "Column": column,

            "Unique Count": unique_count,

            "Unique %": round(
                unique_percentage,
                2
            ),

            "Cardinality": cardinality,

            "Sample Values": ", ".join(
                map(str, sample_values)
            )
        })

    unique_df = pd.DataFrame(unique_data)

    return unique_df