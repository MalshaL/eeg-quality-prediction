"""
This module exports calculated scores into csv
"""

import os.path as op
import pandas as pd


def write_s1(values, headers, idx):
    df = pd.DataFrame(values, columns=headers, index=[idx])
    print(df)
    file = '../../csv_data/s1.csv'
    if op.exists(file):
        df.to_csv(file, mode='a', header=False)
    else:
        df.to_csv(file, header=True)
