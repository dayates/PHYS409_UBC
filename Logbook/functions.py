# some initial things to import
import os
import csv

# numpy and curve_fit
import numpy as np
from scipy.optimize import curve_fit

# for plotting
import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_data(x, y):

    plt.plot(x, y)
    plt.xlabel("x [arb.]")
    plt.ylabel("y [arb.]")