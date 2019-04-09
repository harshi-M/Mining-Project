import dataCleaning as data
import cluster as cluster
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from scipy.spatial.distance import pdist, squareform

positionBasedAttrList = {"ST": ['Crossing', 'Finishing', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'BallControl', 'ShotPower', 'LongShots', 'Positioning', 'Penalties'],
     "LS": ['Crossing', 'Finishing', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'BallControl', 'ShotPower', 'LongShots', 'Positioning', 'Penalties'],
     "RS": ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "LW": ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "LF": ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "CF": ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "RF": ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "RW": ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "LAM": ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "CAM": ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "RAM": ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "LM": ['Crossing', ' ShortPassing', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "LCM": ['Crossing', ' ShortPassing', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "CM": ['Crossing', ' ShortPassing', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties', ' Stamina', ' LongPassing'],
     "RCM": ['Crossing', ' ShortPassing', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties', ' Stamina', ' LongPassing'],
     "RM": ['Crossing', ' ShortPassing', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "LWB": ['Crossing', ' ShortPassing', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties'],
     "LDM": ['ShortPassing', ' LongPassing', ' BallControl', ' Stamina', ' Interceptions', ' Marking', ' StandingTackle'],
     "CDM": ['ShortPassing', ' LongPassing', ' BallControl', ' Stamina', ' Interceptions', ' Marking', ' StandingTackle'],
     "RDM": ['ShortPassing', ' LongPassing', ' BallControl', ' Stamina', ' Interceptions', ' Marking', ' StandingTackle'],
     "RWB":['ShortPassing', ' LongPassing', ' BallControl', ' Stamina', ' Interceptions', ' Marking', ' StandingTackle'],
     "LB":['ShortPassing', ' LongPassing', ' BallControl', ' Stamina', ' Interceptions', ' Marking', ' StandingTackle'],
     "RB": ['ShortPassing', ' LongPassing', ' BallControl', ' Stamina', ' Interceptions', ' Marking', ' StandingTackle'],
     "LCB": ['HeadingAccuracy', ' Aggression', ' Interceptions', ' Marking', ' StandingTackle', ' SlidingTackle'],
     "CB": ['HeadingAccuracy', ' Aggression', ' Interceptions', ' Marking', ' StandingTackle', ' SlidingTackle'],
     "RCB": ['HeadingAccuracy', ' Aggression', ' Interceptions', ' Marking', ' StandingTackle', ' SlidingTackle'],
     "GK": ['GKDiving', ' GKHandling', ' GKKicking', ' GKPositioning', ' GKReflexes']}

getKeysFromPosition = {"LS": [20, 9, 2, 24], "ST": [7, 9, 20, 23, 2], "RS": [20, 9, 23, 11], "LF": [ 24, 2, 10, 11],
"CF": [11, 2], "RF": [24], "LW": [ 11, 21, 10, 9], "RW": [ 11, 21, 10, 9], "LAM": [10], "CAM": [ 10, 11, 12, 21, 4],
"RAM": [ 10], "LM": [11, 2, 21, 4,], "LCM": [27,4,5,13], "CM": [4,18,27,13,3], "RCM": [27,4,5,13], "RM": [21,11,2,4,10],
"LWB": [14,0], "LDM": [27,18,19,13], "CDM": [18,19,27,3,0], "RDM": [27,18,19,13], "RWB": [14,0,3], "LB": [0,14,5,3,18],
"LCB": [22,26,8,15], "CB": [16,22,8,26,15], "RCB": [26,22,8,19], "RB": [14,0,3,5,19], "GK": [1,25,6]}

def showDiff(player, playerSet, replacementIndex, attrList):
    row1 = playerSet.loc[playerSet['ID'] == replacementIndex]
    row2 = playerSet.loc[playerSet['ID'] == player]
    diffSum = 0
    print(row1)
    for columnName in attrList:
        x1 = row1[columnName]
        x2 = row2[columnName]
        
        if(x1.values > x2.values):
            diff = x1.values - x2.values
            diffSum += diff
            print("Player needs to improve " + columnName + " by ")
            print(diff)
            print("points")
    return  diffSum
    
def chooseReplacementInSet(playersSet, ids, player, positionVal):
    originalPlayersSet = playersSet
    attrList = [x.strip(" ") for x in positionBasedAttrList[positionVal] ]
    #if positionVal == "ST":
    playersSet = playersSet.filter(attrList, axis=1)
    #else:
     #   playersSet = playersSet.drop(['ID', 'Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Value', 'Wage', 'Special', 'Preferred Foot', 'International Reputation', 'Weak Foot', 'Skill Moves', 'Work Rate','Body Type', 'Real Face', 'Position', 'Jersey Number', 'Joined', 'Loaned From', 'Contract Valid Until', 'Height', 'Weight', 'Form', 'LS', 'ST', 'RS','LW','LF','CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB','CB','RCB','RB', 'Release Clause'], axis=1)
    playerIndex= ids.index(player)
    distMatrix = list(squareform(pdist(playersSet.values, metric='cityblock'))[playerIndex])
    del distMatrix[playerIndex]
    del ids[playerIndex]
    replacementIndex = distMatrix.index(min(distMatrix))
    #print("player replacement is " +str(ids[replacementIndex]))
    return showDiff(player, originalPlayersSet, ids[replacementIndex], attrList)

def getClosestInClusters(player, positionVal):
    dataFrame = pickle.load(open("pickels/cleanedDataFramePickel",'rb'))
    dataAttributes = pickle.load(open("pickels/cleanedDataAttributesPickel",'rb'))
    groupedDataFrame = pickle.load(open("groupedDataFrame",'rb'))
    clustersSet = getKeysFromPosition[positionVal]
    #clusteringAttributesList = ["Crossing", "Finishing", "HeadingAccuracy", "ShortPassing", "Volleys", "Dribbling", "Curve", "FKAccuracy", "LongPassing", "BallControl", "Acceleration", "SprintSpeed", "Agility", "Reactions", "Balance", "ShotPower", "Jumping", "Stamina", "Strength", "LongShots", "Aggression", "Interceptions", "Positioning", "Vision", "Penalties", "Composure", "Marking", "StandingTackle", "SlidingTackle", "GKDiving", "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"]
    #[kCost, groupedDataFrame] = cluster.clustersBasedOnAttributes(dataFrame, clusteringAttributesList, 28)
    playersArray = []
    for i in clustersSet:
        playersArray.extend(groupedDataFrame.get_group(i)['ID'].unique())        
    playersArray = list(map(int, playersArray))
    #print(playersArray)
    if player in playersArray:
        print("Player can already play as " + positionVal)
        return 0
    playersArray.append(player)
    playerTeamMates = []
    ids = []
    for index, row in dataFrame.iterrows():
        if(row["ID"] in playersArray):
            playerTeamMates.append(list(row))
            ids.append(row["ID"])
         
    playersSet = pd.DataFrame(playerTeamMates, columns=dataAttributes)
    return chooseReplacementInSet(playersSet, ids, player, positionVal)

#clusteringAttributesList = ["Crossing", "Finishing", "HeadingAccuracy", "ShortPassing", "Volleys", "Dribbling", "Curve", "FKAccuracy", "LongPassing", "BallControl", "Acceleration", "SprintSpeed", "Agility", "Reactions", "Balance", "ShotPower", "Jumping", "Stamina", "Strength", "LongShots", "Aggression", "Interceptions", "Positioning", "Vision", "Penalties", "Composure", "Marking", "StandingTackle", "SlidingTackle", "GKDiving", "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"]
#for k in range(1,31):
#[kCost, groupedDataFrame] = cluster.clustersBasedOnAttributes(dataFrame, clusteringAttributesList, 28)
#for i in range(0, 28):
#    print(i)
#    print(groupedDataFrame.get_group(i)['Position'].value_counts())
#    print(groupedDataFrame.get_group(i)['Overall'].mean())