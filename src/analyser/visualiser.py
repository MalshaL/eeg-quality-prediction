
from src.common import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA


min_max_scaler = MinMaxScaler()


def plot_features():
    df, data_np = data_load.get_score_data()
    data_scaled = min_max_scaler.fit_transform(data_np[:, 0:6])
    plt.figure(figsize=(8, 8))
    cdict = {0: 'orange', 1: 'green'}

    for j in range(0, 5):
        ax = plt.subplot(3, 2, j + 1)
        for i in [0, 1]:
            ix = np.where(data_np[:, 6] == i)
            ax.scatter(data_scaled[ix, j], data_scaled[ix, 5],
                       c=cdict[i], s=30, label=i, alpha=0.5, edgecolors='none')
        plt.title(list(df)[j] + " by peak accuracy")
        ax.legend()
        ax.grid(True)
    plt.subplots_adjust(hspace=0.5, wspace=0.4)
    plt.show()


def plot_pca():
    df, data_np = data_load.get_score_data()
    data_scaled = min_max_scaler.fit_transform(data_np[:, 0:5])
    pca_fitted = PCA(n_components=2).fit_transform(data_scaled)
    print(pca_fitted)
    plt.figure()
    cdict = {0: 'orange', 1: 'green'}
    for i in [0, 1]:
        ix = np.where(data_np[:, 6] == i)
        plt.scatter(pca_fitted[ix, 0], pca_fitted[ix, 1], c=cdict[i],
                    s=30, label=i, alpha=0.5, edgecolors='none')
    plt.title('PCA Components')
    plt.legend()
    plt.show()
