"""
This module performs the main functions of loading data, calculating scores and writing them to a csv file.
"""
from src import analyser
from src.feature_gen import *
from src.analyser import *
from src.common import data_load


dataset_1 = "robinson-2019"
dataset_2 = "grootswagers-2019"
dataset_3_1 = "grootswagers-2021-1"
dataset_3_2 = "grootswagers-2021-2"


def process_subject(dataset, sub):
    raw_data = data_load.get_data(dataset, sub)
    np_data = raw_data.get_data()
    channels = raw_data.info['ch_names']
    s1_general_amplitude.get_score(dataset, sub, np_data, channels)
    s2_alpha_amplitude.get_score(dataset, sub, np_data, channels)
    s4_beta_amplitude.get_score(dataset, sub, np_data)
    s6_theta_amplitude.get_score(dataset, sub, np_data)


# process_subject(dataset_3_2, "20")
# cv for regression, nearest neighbor classifier, scores
# report

# subs = ["02", "03", "04", "05", "06", "07", "08", "09"]
# for i in subs:
#     process_subject(dataset_3_2, i)

# for i in range(10, 21):
#     process_subject(dataset_3_2, str(i))


# regressor.lin_regression()
classifier.nb_classifier(dataset_1)
classifier.nb_classifier(dataset_2)
classifier.nb_classifier(dataset_3_1)
classifier.nb_classifier(dataset_3_2)
