# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

from functions import line2list


class DataPlotter(object):
    def __init__(self, filename, field=' ', dtype=float):
        """
        Create a pure data file class.

        Example:

        >>> a = DataPlotter(filename='DOS1')

        Class attributes descriptions
        =======================================================
          Attribute      Description
          ============  =======================================
          filename       string, name of the SPLITED DOS file
          field          string, separator of a line
          dtype          type, convertion type of data
          ============  =======================================
        """
        self.filename = filename
        self.field = field
        self.dtype = dtype
        #load data
        self.load()

    def load(self):
        "Load all data in file into array."
        data = []
        with open(self.filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line[0].isdigit():  # comment line or not
                    if not line.startswith('-'):
                        continue
                    elif not line[1].isdigit():
                        continue
                linedata = line2list(line, field=self.field,
                                     dtype=self.dtype)
                data.append(linedata)
        self.data = np.array(data)

        return data

    def plot2d(self, xcol, ycols):
        "显示特定两列数据"
        '''
        Parameter
        ---------
        xcol: int
            column number of data for x values
        ycols: tuple of int
            column numbers of data for y values
            (start, stop[, step])
        Example:
        >>> a.plot2d(0, (1, 3, 1))
        '''
        x = self.data[:, xcol]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in xrange(*ycols):
            y = self.data[:, i]
            ax.plot(x, y, linewidth=3)

        fig.show()

    def plotall(self):
        "将所有数据一起显示"
        ncols = self.data.shape[1]
        x = self.data[:, 0]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for col in xrange(1, ncols):
            y = self.data[:, col]
            ax.plot(x, y, linewidth=3)
        fig.show()
