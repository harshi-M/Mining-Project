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
k = 14
[kCost, groupedDataFrame, dataFrame] = cluster.clustersBasedOnAttributes(dataFrame, clusteringAttributesList, k)  
x.append(k)
y.append(kCost)
print(str(k)+": "+str(kCost))

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(dataFrame[clusteringAttributesList])
principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, dataFrame[['Clusters']]], axis = 1)

clusters = list(set(dataFrame['Clusters'].values))
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = clusters
colors = np.random.rand(len(clusters))
for target, color in zip(targets,colors):
    indicesToKeep = dataFrame['Clusters'] = target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
            finalDf.loc[indicesToKeep, 'principal component 2'], c = color)
ax.legend(targets)
ax.grid()
plt.show()