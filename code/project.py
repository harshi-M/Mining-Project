import dataCleaning as data
import cluster as cluster
import matplotlib.pyplot as plt
import pickle


[dataFrame, dataArray, dataAttributes] = data.getDataFrame("data/cleanedData.csv")
pickle.dump(dataFrame, open("cleanedDataDataFramePickel",'wb'))
pickle.dump(dataArray, open("cleanedDataDataArrayPickel",'wb'))
pickle.dump(dataAttributes, open("cleanedDataDataAttributesPickel",'wb'))

# dataFrame = pickle.load(open("cleanedDataDataFramePickel",'rb'))
# dataArray = pickle.load(open("cleanedDataDataArrayPickel",'rb'))
# dataAttributes = pickle.load(open("cleanedDataDataAttributesPickel",'rb'))
print(dataFrame.to_string())
clusteringAttributesList = ["Crossing", "Finishing", "HeadingAccuracy", "ShortPassing", "Volleys", "Dribbling", "Curve", "FKAccuracy", "LongPassing", "BallControl", "Acceleration", "SprintSpeed", "Agility", "Reactions", "Balance", "ShotPower", "Jumping", "Stamina", "Strength", "LongShots", "Aggression", "Interceptions", "Positioning", "Vision", "Penalties", "Composure", "Marking", "StandingTackle", "SlidingTackle", "GKDiving", "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"]
x = []
y  = []
for k in range(15,30):
    [kCost, clusters] = cluster.clustersBasedOnAttributes(dataFrame, clusteringAttributesList, k)  
    x.append(k)
    y.append(kCost)
    print(str(k)+": "+str(kCost))
    break
plt.title('k Costs')
plt.ylabel('cost')
plt.xlabel('k')
plt.plot(x, y)
plt.show()