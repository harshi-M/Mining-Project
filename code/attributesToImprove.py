import dataCleaning as data
import cluster as cluster
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from scipy.spatial.distance import pdist, squareform


# [dataFrame, dataArray, dataAttributes] = data.getDataFrame("data/cleanedData.csv")
# pickle.dump(dataFrame, open("cleanedDataDataFramePickel",'wb'))
# pickle.dump(dataArray, open("cleanedDataDataArrayPickel",'wb'))
# pickle.dump(dataAttributes, open("cleanedDataDataAttributesPickel",'wb'))

def getKeysFromPosition(position):
    print(position)
    x = []
    if position == "LS":
        x.append(20)
        x.append(9)
        x.append(2)
        x.append(24)
    elif position == "ST":
        x.append(7)
        x.append(9)
        x.append(20)
        x.append(23)
        x.append(2)
    elif position == "RS":
        x.append(20)
        x.append(9)
        x.append(23)
        x.append(11)
    elif position == "LF": #dicey
        x.append(24)
        x.append(2)
        x.append(10)
        x.append(11)
    elif position == "CF":
        x.append(11)
        x.append(2)
    elif position == "RF":
        x.append(24)
    elif position == "LW":
        x.append(11)
        x.append(21)
        x.append(10)
        x.append(9)
    elif position == "RW":
        x.append(11)
        x.append(21)
        x.append(10)
        x.append(9)
    elif position == "LAM":
        x.append(10)
    elif position == "CAM":
        x.append(10)
        x.append(11)
        x.append(12)
        x.append(21)
        x.append(4)
    elif position == "RAM":
        x.append(10)
    elif position == "LM":
        x.append(11)
        x.append(2)
        x.append(21)
        x.append(4)
    elif position == "LCM":
        x.append(27)
        x.append(4)
        x.append(5)
        x.append(13)
    elif position == "CM":
        x.append(4)
        x.append(18)
        x.append(27)
        x.append(13)
        x.append(3)
    elif position == "RCM":
        x.append(27)
        x.append(4)
        x.append(5)
        x.append(13)
    elif position == "RM":
        x.append(21)
        x.append(11)
        x.append(2)
        x.append(4)
        x.append(10)
    elif position == "LWB":
        x.append(14)
        x.append(0)
    elif position == "LDM":
        x.append(27)
        x.append(18)
        x.append(19)
        x.append(13)
    elif position == "CDM":
        x.append(18)
        x.append(19)
        x.append(27)
        x.append(3)
        x.append(0)
    elif position == "RDM":
        x.append(27)
        x.append(18)
        x.append(19)
        x.append(13)
    elif position == "RWB":
        x.append(14)
        x.append(0)
        x.append(3)
    elif position == "LB":
        x.append(0)
        x.append(14)
        x.append(5)
        x.append(3)
        x.append(18)
    elif position == "LCB":
        x.append(22)
        x.append(26)
        x.append(8)
        x.append(15)
    elif position == "CB":
        x.append(16)
        x.append(22)
        x.append(8)
        x.append(26)
        x.append(15)
    elif position == "RCB":
        x.append(26)
        x.append(22)
        x.append(8)
        x.append(19)
    elif position == "RB":
        x.append(14)
        x.append(0)
        x.append(3)
        x.append(5)
        x.append(19)
    elif position == "GK":
        x.append(1)
        x.append(25)
        x.append(6)
    return x

def showDiff(player, playerSet, replacementIndex, attrList):
    row1 = playerSet.loc[playerSet['ID'] == replacementIndex]
    row2 = playerSet.loc[playerSet['ID'] == player]
    
    #print(row1)
    #print(row2)
    
    print(row1)
    for columnName in attrList:
        x1 = row1[columnName]
        x2 = row2[columnName]
        
        if(x1.values > x2.values):
            print("Player needs to improve " + columnName + " by ")
            print(x1.values - x2.values)
            print("points")
    
    return

def getAttrList(positionVal):
    if positionVal == "ST":
        return ['Crossing', 'Finishing', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'BallControl', 'ShotPower', 'LongShots', 'Positioning', 'Penalties']
    elif positionVal == "LS":
        return ['Crossing', 'Finishing', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'BallControl', 'ShotPower', 'LongShots', 'Positioning', 'Penalties']
    elif positionVal == "RS":
        return ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "LW":
        return ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "LF":
        return ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "CF":
        return ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "RF":
        return ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "RW":
        return ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "LAM":
        return ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "CAM":
        return ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "RAM":
        return ['Crossing', ' Finishing', ' ShortPassing', ' Volleys', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "LM":
        return ['Crossing', ' ShortPassing', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "LCM":
        return ['Crossing', ' ShortPassing', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "CM":
        return ['Crossing', ' ShortPassing', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties', ' Stamina', ' LongPassing']
    elif positionVal == "RCM":
        return ['Crossing', ' ShortPassing', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties', ' Stamina', ' LongPassing']
    elif positionVal == "RM":
        return ['Crossing', ' ShortPassing', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "LWB":
        return ['Crossing', ' ShortPassing', ' Dribbling', ' Curve', ' BallControl', ' ShotPower', ' LongShots', ' Positioning', ' Penalties']
    elif positionVal == "LDM":
        return ['ShortPassing', ' LongPassing', ' BallControl', ' Stamina', ' Interceptions', ' Marking', ' StandingTackle']
    elif positionVal == "CDM":
        return ['ShortPassing', ' LongPassing', ' BallControl', ' Stamina', ' Interceptions', ' Marking', ' StandingTackle']
    elif positionVal == "RDM":
        return ['ShortPassing', ' LongPassing', ' BallControl', ' Stamina', ' Interceptions', ' Marking', ' StandingTackle']
    elif positionVal == "RWB":
        return ['ShortPassing', ' LongPassing', ' BallControl', ' Stamina', ' Interceptions', ' Marking', ' StandingTackle']
    elif positionVal == "LB":
        return ['ShortPassing', ' LongPassing', ' BallControl', ' Stamina', ' Interceptions', ' Marking', ' StandingTackle']
    elif positionVal == "RB":
        return ['ShortPassing', ' LongPassing', ' BallControl', ' Stamina', ' Interceptions', ' Marking', ' StandingTackle']
    elif positionVal == "LCB":
        return ['HeadingAccuracy', ' Aggression', ' Interceptions', ' Marking', ' StandingTackle', ' SlidingTackle']
    elif positionVal == "CB":
        return ['HeadingAccuracy', ' Aggression', ' Interceptions', ' Marking', ' StandingTackle', ' SlidingTackle']
    elif positionVal == "RCB":
        return ['HeadingAccuracy', ' Aggression', ' Interceptions', ' Marking', ' StandingTackle', ' SlidingTackle']
    elif positionVal == "GK":
        return ['GKDiving', ' GKHandling', ' GKKicking', ' GKPositioning', ' GKReflexes']
    
    
def chooseReplacementInSet(playersSet, ids, player, positionVal):
    originalPlayersSet = playersSet
    attrList = [x.strip(" ") for x in getAttrList(positionVal) ]
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
    showDiff(player, originalPlayersSet, ids[replacementIndex], attrList)
    return

def getClosestInClusters(player, positionVal):
    dataFrame = pickle.load(open("cleanedDataDataFramePickel",'rb'))
    dataAttributes = pickle.load(open("cleanedDataDataAttributesPickel",'rb'))
    groupedDataFrame = pickle.load(open("groupedDataFrame",'rb'))
    clustersSet = getKeysFromPosition(positionVal)
    
    #clusteringAttributesList = ["Crossing", "Finishing", "HeadingAccuracy", "ShortPassing", "Volleys", "Dribbling", "Curve", "FKAccuracy", "LongPassing", "BallControl", "Acceleration", "SprintSpeed", "Agility", "Reactions", "Balance", "ShotPower", "Jumping", "Stamina", "Strength", "LongShots", "Aggression", "Interceptions", "Positioning", "Vision", "Penalties", "Composure", "Marking", "StandingTackle", "SlidingTackle", "GKDiving", "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"]

    #[kCost, groupedDataFrame] = cluster.clustersBasedOnAttributes(dataFrame, clusteringAttributesList, 28)

    playersArray = []
    
    for i in clustersSet:
        playersArray.extend(groupedDataFrame.get_group(i)['ID'].unique())
        
    playersArray = list(map(int, playersArray))

    #print(playersArray)

    if player in playersArray:
        print("Player can already play as " + positionVal)
        return
    
    playersArray.append(player)
    playerTeamMates = []
    ids = []
    for index, row in dataFrame.iterrows():
        if(row["ID"] in playersArray):
            playerTeamMates.append(list(row))
            ids.append(row["ID"])
         
    playersSet = pd.DataFrame(playerTeamMates, columns=dataAttributes)
    chooseReplacementInSet(playersSet, ids, player, positionVal)
    return

player = int(input("Enter player id "))
positionVal = input("Enter position he wants to play in ")
getClosestInClusters(player, positionVal)


#clusteringAttributesList = ["Crossing", "Finishing", "HeadingAccuracy", "ShortPassing", "Volleys", "Dribbling", "Curve", "FKAccuracy", "LongPassing", "BallControl", "Acceleration", "SprintSpeed", "Agility", "Reactions", "Balance", "ShotPower", "Jumping", "Stamina", "Strength", "LongShots", "Aggression", "Interceptions", "Positioning", "Vision", "Penalties", "Composure", "Marking", "StandingTackle", "SlidingTackle", "GKDiving", "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"]
#for k in range(1,31):
#[kCost, groupedDataFrame] = cluster.clustersBasedOnAttributes(dataFrame, clusteringAttributesList, 28)
#for i in range(0, 28):
#    print(i)
#    print(groupedDataFrame.get_group(i)['Position'].value_counts())
#    print(groupedDataFrame.get_group(i)['Overall'].mean())