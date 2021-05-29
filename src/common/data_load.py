""" Read EEG data files
This module reads the data from EEG data files for each subject and returns mne.Raw objects.
"""

from src.common import csv_export
import pandas as pd
import os.path as op
from mne.io import read_raw_brainvision


data_dir = "/Users/malsharanawaka/Documents/Masters/Sem3/PPA/data"


def get_data(dataset, sub):
    data_file = op.join(data_dir, dataset, "sub-"+sub+"/eeg/sub-"+sub+"_task-rsvp_eeg.vhdr")
    # renamed_file = op.join(data_dir, "sub-"+sub+"/eeg/sub-"+sub+"_renamed.vhdr")
    # copyfile_brainvision(original_file, renamed_file, verbose=True)
    # event_file = op.join(data_dir, "sub-"+sub+"/eeg/sub-"+sub+"_task-rsvp_events.tsv")
    # event_onset = pd.read_csv(event_file, sep='\t')['onset']
    raw_data = read_raw_brainvision(data_file, preload=True, scale=10**6)
    # l_freq=0.1 to use a high pass filter to remove the drift in data
    return raw_data.filter(l_freq=0.1, h_freq=None)


def get_score_data(dataset, score_filename):
    scores = '1', '2', '4', '6'
    file = csv_export.combine_csv(dataset, scores, score_filename)
    df = pd.read_csv(file)
    return df, df.to_numpy()
