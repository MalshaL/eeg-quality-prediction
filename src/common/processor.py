"""
This module performs the main functions of loading data, calculating scores and writing them to a csv file.
"""

from src.feature_gen import *
from src.common import *


def process_subject(sub):
    raw_data = data_load.get_data(sub)
    np_data = raw_data.get_data()
    channels = raw_data.info['ch_names']
    s1_general_amplitude.get_score(sub, np_data, channels)
    # print(get_highest_alpha_amplitude(np_data, channels))
    # print(get_beta_amplitude_score(np_data))
    # print(s6_theta_amplitude.get_score(np_data))


process_subject("20")
