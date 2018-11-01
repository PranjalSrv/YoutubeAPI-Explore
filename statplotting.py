import matplotlib.pyplot as plt
import numpy as np

def plottingViews(views):
    plt.bar(np.arange(len(views)),views, facecolor = 'g')

    plt.show()