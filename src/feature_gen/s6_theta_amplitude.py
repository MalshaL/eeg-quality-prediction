"""
This module calculates the highest amplitude score based on the theta band of the signal
"""

from mne.filter import filter_data


def get_theta_band(np_data):
    return filter_data(np_data, sfreq=1000, l_freq=4, h_freq=8, method='iir')


# score 6
def get_score(np_data):
    theta_data = get_theta_band(np_data)
    max_amp = 30
    scores = []
    for row in theta_data:
        amp_count = sum(abs(i) < max_amp for i in row)
        scores.append(amp_count / len(row))
    return sum(scores) / len(scores)