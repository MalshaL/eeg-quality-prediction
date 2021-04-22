import os.path as op
import numpy as np
import pandas as pd
import mne
from mne.filter import filter_data
import matplotlib.pyplot as plt


plt.rc('font', size=8)
plt.rc('axes', titlesize=8, labelsize=8)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('legend', fontsize=8)
plt.rc('figure', titlesize=8)
data_dir = "/Users/malsharanawaka/Documents/Masters/Sem3/PPA/rapidmvpa-soa-duration"


def load_data(sub):
    data_file = op.join(data_dir, "sub-"+sub+"/eeg/sub-"+sub+"_task-rsvp_eeg.vhdr")
    # renamed_file = op.join(data_dir, "sub-"+sub+"/eeg/sub-"+sub+"_renamed.vhdr")
    # copyfile_brainvision(original_file, renamed_file, verbose=True)
    event_file = op.join(data_dir, "sub-"+sub+"/eeg/sub-"+sub+"_task-rsvp_events.tsv")
    event_onset = pd.read_csv(event_file, sep='\t')['onset']
    raw_data = mne.io.read_raw_brainvision(data_file, preload=True, scale=10**6)
    # l_freq=0.1 to use a high pass filter to remove the drift in data
    return raw_data.filter(l_freq=0.1, h_freq=None)


def plot_psd(data):
    for raw_data in data:
        raw_data.plot_psd(fmax=50)


def plot_channels(data, channel_list):
    for raw_data in data:
        raw_data.plot(n_channels=63)


# amplitudes = np.absolute(np.fft.rfft(row))
# frequencies = np.fft.rfftfreq(len(row), 1.0/freq)


def get_alpha_band(np_data):
    return filter_data(np_data, sfreq=1000, l_freq=8, h_freq=12, method='iir')


def get_beta_band(np_data):
    return filter_data(np_data, sfreq=1000, l_freq=12, h_freq=40, method='iir')


def get_theta_band(np_data):
    return filter_data(np_data, sfreq=1000, l_freq=4, h_freq=8, method='iir')


# score 6
def get_theta_amplitude_score(np_data):
    theta_data = get_theta_band(np_data)
    max_amp = 30
    scores = []
    for row in theta_data:
        amp_count = sum(abs(i) < max_amp for i in row)
        scores.append(amp_count / len(row))
    return sum(scores) / len(scores)


# score 5
def get_beta_sinusoidal_score(np_data):
    beta_data = get_beta_band(np_data)


# score 4
def get_beta_amplitude_score(np_data):
    beta_data = get_beta_band(np_data)
    print(np_data.shape)
    print(beta_data.shape)
    max_amp = 20
    scores = []
    for row in beta_data:
        amp_count = sum(abs(i) < max_amp for i in row)
        scores.append(amp_count/len(row))
    return sum(scores)/len(scores)


# score 3
def get_dominant_alpha_amplitude(np_data):
    alpha_data = get_alpha_band(np_data)
    # for row in alpha_data:



# score 2
def get_highest_alpha_amplitude(np_data, channels):
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


# score 1
def get_general_amplitude_score(subject, np_data, channels):
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
    plt.savefig("%s.pdf" % subject, bbox_inches='tight', pad_inches=0, dpi=1200)


def process_subject(sub):
    raw_data = load_data(sub)
    np_data = raw_data.get_data()
    channels = raw_data.info['ch_names']
    # get_general_amplitude_score("sub_%s" % sub, np_data, channels)
    # print(get_highest_alpha_amplitude(np_data, channels))
    # print(get_beta_amplitude_score(np_data))
    print(get_theta_amplitude_score(np_data))


if __name__ == '__main__':
    process_subject("07")

    # print(onset_05.head())
    # print(raw_05.info)
    # freq = raw_05.info['sfreq']
    # num of time samples
    # print(raw_05.n_times)
    # times at which signals are present
    # print(raw_05.times)

    # plot power spectral density
    # plot_psd([raw_05, raw_07])

    # get index of sample occurring closest to 2s timestamp
    # print(raw_05.time_as_index(onset_05[4]))
    # raw = NumPy array of shape (n_channels, n_timepoints)
    # len(raw) = number of timepoints
    # raw.info['sfreq'] = sampling frequency
    # data_05, times_05 = raw_05.get_data(return_times=True)
    # print(data_05.shape)
    # print(np.amax(data_07, axis=1)*1000*1000)

