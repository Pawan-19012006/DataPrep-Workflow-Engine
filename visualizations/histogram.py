import matplotlib.pyplot as plt
import seaborn as sns

def histogram_plot(df, column):

    fig, ax = plt.subplots(figsize=(7, 4))

    sns.histplot(
        df[column],
        kde=True,
        ax=ax
    )

    ax.set_title(f"{column} Distribution")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")

    return fig