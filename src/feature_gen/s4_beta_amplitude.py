"""
This module calculates the beta amplitude score based on the beta band of the signal
"""

from mne.filter import filter_data


def get_beta_band(np_data):
    return filter_data(np_data, sfreq=1000, l_freq=12, h_freq=40, method='iir')


# score 4
def get_score(np_data):
    beta_data = get_beta_band(np_data)
    print(np_data.shape)
    print(beta_data.shape)
    max_amp = 20
    scores = []
    for row in beta_data:
        amp_count = sum(abs(i) < max_amp for i in row)
        scores.append(amp_count/len(row))
    return sum(scores)/len(scores)