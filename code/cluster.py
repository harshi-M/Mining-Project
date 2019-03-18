from sklearn.cluster import KMeans
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

def getSubDataFrame(dataFrame, attribuetesList):
    return dataFrame[attribuetesList]

def printGroupedDataFrame(groupedDataFeame):
    clusterNum = 1
    for key, item in groupedDataFeame:
        print("cluster number = "+ str(clusterNum))
        print(groupedDataFeame.get_group(key).to_string(), "\n\n")
        clusterNum+= 1
    return

def clustersBasedOnAttributes(dataFrame, attribuetesList, k):
    print("k Value is : "+str(k))
    dataFrame = shuffle(dataFrame)
    subDataFrame = getSubDataFrame(dataFrame, attribuetesList)
    subDataFrame = scale(subDataFrame)
    kmeans = KMeans(n_clusters=k).fit(subDataFrame)
    dataFrame['Clusters'] = kmeans.labels_
    groupedDataFrame = dataFrame.groupby('Clusters')
    printGroupedDataFrame(groupedDataFrame)
    print("++++++++++++++++++++++++++++\n\n\n")
    return [kmeans.inertia_, groupedDataFrame]
