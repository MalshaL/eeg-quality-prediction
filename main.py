

def plot_psd(data):
    for raw_data in data:
        raw_data.plot_psd(fmax=50)


def plot_channels(data, channel_list):
    for raw_data in data:
        raw_data.plot(n_channels=63)


# amplitudes = np.absolute(np.fft.rfft(row))
# frequencies = np.fft.rfftfreq(len(row), 1.0/freq)


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

