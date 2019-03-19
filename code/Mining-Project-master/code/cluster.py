from sklearn.cluster import KMeans
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

def getSubDataFrame(dataFrame, attribuetesList):
    return dataFrame[attribuetesList]

def printGroupedDataFrame(groupedDataFeame):
    for key, item in groupedDataFeame:
        print(groupedDataFeame.get_group(key).to_string(), "\n\n")
    return

def clustersBasedOnAttributes(dataFrame, attribuetesList, k):
    print("k Value is : "+str(k))
    dataFrame = shuffle(dataFrame)
    subDataFrame = getSubDataFrame(dataFrame, attribuetesList)
    subDataFrame = scale(subDataFrame)
    kmeans = KMeans(n_clusters=k).fit(subDataFrame)
    dataFrame['Clusters'] = kmeans.labels_
    groupedDataFrame = dataFrame.groupby('Clusters')
    if k==17:
        printGroupedDataFrame(groupedDataFrame)
    print("++++++++++++++++++++++++++++\n\n\n")
    return [kmeans.inertia_, groupedDataFrame]
