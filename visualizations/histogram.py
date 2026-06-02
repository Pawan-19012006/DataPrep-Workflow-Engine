import matplotlib.pyplot as plt
import seaborn as sns

def histogram_plot(df, column):

    fig, ax = plt.subplots(figsize=(8, 6.7))

    sns.histplot(
        df[column],
        kde=True,
        ax=ax,
        bins=30
    )

    ax.set_title(f"{column} Distribution")

    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

    plt.tight_layout()

    return fig