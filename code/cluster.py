from sklearn.cluster import KMeans
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

def getSubDataFrame(dataFrame, attribuetesList):
    return dataFrame[attribuetesList]

def clustersBasedOnAttributes(dataFrame, attribuetesList, k):
    dataFrame = shuffle(dataFrame)
    subDataFrame = getSubDataFrame(dataFrame, attribuetesList)
    subDataFrame = scale(subDataFrame)

    kmeans = KMeans(n_clusters=k).fit(subDataFrame)
    labels = kmeans.labels_
    dataFrame['clusters'] = labels
    print(dataFrame.to_string())
    clusters = []
    kCost = 0
    return [kCost, clusters]
