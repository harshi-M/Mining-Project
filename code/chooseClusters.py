import dataCleaning as data
import cluster as cluster
import matplotlib.pyplot as plt
import pickle
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

# [dataFrame, dataArray, dataAttributes] = data.getDataFrame("data/cleanedData.csv")
# pickle.dump(dataFrame, open("pickels/cleanedDataFramePickel",'wb'))
# pickle.dump(dataArray, open("pickels/cleanedDataArrayPickel",'wb'))
# pickle.dump(dataAttributes, open("pickels/cleanedDataAttributesPickel",'wb'))

dataFrame = pickle.load(open("pickels/cleanedDataFramePickel",'rb'))
dataArray = pickle.load(open("pickels/cleanedDataArrayPickel",'rb'))
dataAttributes = pickle.load(open("pickels/cleanedDataAttributesPickel",'rb'))

# print(list(set(dataFrame['Position'].values)))

clusteringAttributesList = ["Crossing", "Finishing", "HeadingAccuracy", "ShortPassing", "Volleys", "Dribbling", "Curve", "FKAccuracy", "LongPassing", "BallControl", "Acceleration", "SprintSpeed", "Agility", "Reactions", "Balance", "ShotPower", "Jumping", "Stamina", "Strength", "LongShots", "Aggression", "Interceptions", "Positioning", "Vision", "Penalties", "Composure", "Marking", "StandingTackle", "SlidingTackle", "GKDiving", "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"]
x = []
y  = []
for k in range(1, 15):
    [kCost, groupedDataFrame, dataFrame] = cluster.clustersBasedOnAttributes(dataFrame, clusteringAttributesList, k)  
    x.append(k)
    y.append(kCost)
    print(str(k)+": "+str(kCost))
plt.title('k Costs')
plt.ylabel('cost')
plt.xlabel('k')
plt.plot(x, y, marker='o', linestyle='--')
plt.grid()
plt.show()
