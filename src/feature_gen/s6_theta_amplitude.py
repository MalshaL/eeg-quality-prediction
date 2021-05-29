"""
This module calculates the highest amplitude score based on the theta band of the signal
"""

from mne.filter import filter_data
from src.common import csv_export


def get_theta_band(np_data):
    return filter_data(np_data, sfreq=1000, l_freq=4, h_freq=8, method='iir')


# score 6
def get_score(dataset, subject, np_data):
    theta_data = get_theta_band(np_data)
    max_amp = 30
    scores = []
    for row in theta_data:
        amp_count = sum(abs(i) < max_amp for i in row)
        scores.append(amp_count / len(row))
    score = sum(scores) / len(scores)
    csv_export.write_data("6", [[score]], ['theta_amp'], dataset, subject)
