import matplotlib.pyplot as plt
import seaborn as sns

def heatmap_plot(df, selected_cols):

    corr_matrix = df[selected_cols].corr()

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    ax.set_title("Correlation Heatmap")

    return fig