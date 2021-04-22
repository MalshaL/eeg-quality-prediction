"""
This module calculates the general amplitude score
"""

import numpy as np
import matplotlib.pyplot as plt


plt.rc('font', size=8)
plt.rc('axes', titlesize=8, labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)


# score 1
def get_score(subject, np_data, channels):
    bin_width = 1000
    j = 1
    plt.figure(figsize=(11.69, 16.53))
    for row in np_data:
        plt.subplot(13, 5, j)
        print(np.amax(row))
        bin_count = int(round(len(row)/bin_width))
        bin_sums, bin_edges = np.histogram(row, bins=bin_count)
        mask = (-100 <= bin_edges) & (bin_edges <= 100)
        normal_bins = bin_sums[mask[:-1]][:-1]
        score_1 = normal_bins.sum()/bin_sums.sum()

        normal_positive_mask = (0 < bin_edges) & (bin_edges <= 100)
        normal_positive_bins = bin_sums[normal_positive_mask[:-1]][:-1]
        positive_mask = (0 < bin_edges)
        positive_bins = bin_sums[positive_mask[:-1]][:-1]
        score_2 = normal_positive_bins.sum()/positive_bins.sum()
        score = ((score_1+score_2)/2)*100

        plt.bar(bin_edges[:-1], bin_sums, color='g')
        plt.title(channels[j-1] + " - Score: %.2f" % score)
        j += 1
    plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0.7, wspace=0.4)
    plt.margins(0, 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig(".../.../plots/s1/%s.pdf" % subject, bbox_inches='tight', pad_inches=0, dpi=1200)