import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def create_annotated_posneg_heatmap(ax, data):
    """
    Creates an annotated positive-negative heatmap.

    Parameters:
        - ax: The axis object to plot the heatmap.
        - data: The 2D array of data for the heatmap.

    Returns:
        The modified axis object and the colorbar object.
    """
    cmap = mcolors.TwoSlopeNorm(vcenter=0)
    im = ax.imshow(data, cmap='bwr', norm=cmap)
    cbar = ax.figure.colorbar(im, ax=ax)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            text = ax.text(j, i, f"{data[i, j]:.2f}", ha="center", va="center", color="k")
    ax.set_aspect('auto')
    return ax, cbar

if __name__ == "__main__":
    data = np.random.randn(5, 5)  # Random data for demonstration
    print(data)
    fig, ax = plt.subplots()
    create_annotated_posneg_heatmap(ax, data)
    plt.show()
