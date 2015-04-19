"""
paq2py
Lloyd Russell 2015
"""

import numpy as np


def paq_read(file_path=None, plot=False):
    """
    Read binary *.paq file (from PackIO)
    Lloyd Russell 2015

    Parameters
    ----------
    file_path : str
        path to file to read in. if none supplied use GUI load dialog,
        buggy on mac osx - Tk/matplotlib.
    plot : bool
        plot the read data? (optional, default = False)

    Returns
    -------
    data : ndarray
    chan_names : list
    units : list
    rate : int
    """
    if file_path is None:
        import Tkinter
        import tkFileDialog
        root = Tkinter.Tk()
        root.withdraw()
        file_path = tkFileDialog.askopenfilename()
        root.destroy()

    # open file
    fid = open(file_path, 'rb')

    # get sample rate
    rate = int(np.fromfile(fid, dtype='>f', count=1))

    # get number of channels
    num_chans = int(np.fromfile(fid, dtype='>f', count=1))

    # get channel names
    chan_names = []
    for i in range(num_chans):
        num_chars = int(np.fromfile(fid, dtype='>f', count=1))
        chan_name = ''
        for j in range(num_chars):
            chan_name = chan_name + chr(np.fromfile(fid, dtype='>f', count=1))
        chan_names.append(chan_name)

    # get channel hardware lines
    hw_chans = []
    for i in range(num_chans):
        num_chars = int(np.fromfile(fid, dtype='>f', count=1))
        hw_chan = ''
        for j in range(num_chars):
            hw_chan = hw_chan + chr(np.fromfile(fid, dtype='>f', count=1))
        hw_chans.append(hw_chan)

    # get acquisition units
    units = []
    for i in range(num_chans):
        num_chars = int(np.fromfile(fid, dtype='>f', count=1))
        unit = ''
        for j in range(num_chars):
            unit = unit + chr(np.fromfile(fid, dtype='>f', count=1))
        units.append(unit)

    # get data
    temp_data = np.fromfile(fid, dtype='>f', count=-1)
    num_datapoints = len(temp_data)/num_chans
    data = np.reshape(temp_data, [num_datapoints, num_chans]).transpose()

    # close file
    fid.close()

    if plot:
        import matplotlib.pylab as plt
        f, axes = plt.subplots(num_chans, 1, sharex=True)
        for idx, ax in enumerate(axes):
            ax.plot(data[idx])
            ax.set_xlim([0, num_datapoints-1])
            # ax.xticks(range(num_datapoints), range(num_datapoints/rate))
            ax.set_ylabel(units[idx])
            ax.set_title(chan_names[idx])
        plt.show()

    return data, chan_names, units, rate
