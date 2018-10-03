import matplotlib.pyplot as plt
import numpy as np

#def plottingViews(statistics):
def plottingViews(views):
    #print(statistics)
    #views = [i['viewCount'] for i in statistics]

    #views = [8900,7521,6204,9617,5225,1678,5343,2851,9440,2890]
    plt.bar(np.arange(len(views)),views, facecolor = 'g')

    #plt.grid(True)
    plt.show()

