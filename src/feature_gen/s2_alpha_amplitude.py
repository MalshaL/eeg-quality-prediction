"""
This module calculates the highest amplitude score based on the alpha band of the signal
"""

import numpy as np
from mne.filter import filter_data


def get_alpha_band(np_data):
    return filter_data(np_data, sfreq=1000, l_freq=8, h_freq=12, method='iir')


# score 2
def get_score(np_data, channels):
    alpha_data = get_alpha_band(np_data)
    print(alpha_data.shape)
    # get maximum amp of each channel
    highest_amps = [np.amax(row) for row in alpha_data]
    amp_dict = {k: v for k, v in zip(channels, highest_amps)}
    sorted_amps = {k: v for k, v in sorted(amp_dict.items(), key=lambda item: item[1])}
    excluded_channels = ['Fp1', 'Fp2', 'AFz', 'AF3', 'AF4', 'AF7', 'AF8',
                         'Fz', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
                         'FCz', 'FC1', 'FC2', 'FC3', 'FC4', 'FC5', 'FC6', 'FT7', 'FT8']
    picked_channels = [ch for ch in channels if ch not in excluded_channels]
    print(len(picked_channels))
    score = 0
    for ch in picked_channels:
        sorted_index = list(sorted_amps.keys()).index(ch)
        if sorted_index > len(channels)/2:
            score += 1
        elif sorted_index > len(channels)/4:
            score += 0.5
    return (score/10)*100