"""
This module exports calculated scores into csv
"""

import os.path as op
import pandas as pd


directory = '../../csv_data/'


def write_data(score_num, values, headers, dataset, idx):
    df = pd.DataFrame(values, columns=headers, index=[idx])
    print(df)
    file = '%s%s/s%s.csv' % (directory, dataset, score_num)
    if op.exists(file):
        df.to_csv(file, mode='a', header=False)
    else:
        df.to_csv(file, header=True)


def combine_csv(dataset, score_num_list, score_filename):
    files = []
    for score_num in score_num_list:
        files.append('%s%s/s%s.csv' % (directory, dataset, score_num))
    df = pd.concat((pd.read_csv(file, index_col=0) for file in files), axis=1)
    df['peak_acc'] = (pd.read_csv('%s%s/%s.csv' % (directory, dataset, score_filename))['peak_acc']).values
    df['is_good'] = (pd.read_csv('%s%s/%s.csv' % (directory, dataset, score_filename))['is_good']).values

    combined_file = '%s%s/combined.csv' % (directory, dataset)
    df.to_csv(combined_file, header=True, index=False)
    return combined_file
