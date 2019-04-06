import pickle
import pandas as pd
from scipy.spatial.distance import pdist, squareform

def chooseReplacementInSet(playersSet, ids, player):
    playersSet = playersSet.drop(['ID', 'Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Value', 'Wage', 'Special', 'Preferred Foot', 'International Reputation', 'Weak Foot', 'Skill Moves', 'Work Rate','Body Type', 'Real Face', 'Position', 'Jersey Number', 'Joined', 'Loaned From', 'Contract Valid Until', 'Height', 'Weight', 'Form', 'LS', 'ST', 'RS','LW','LF','CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB','CB','RCB','RB', 'Release Clause'], axis=1)
    playerIndex= ids.index(player)
    distMatrix = list(squareform(pdist(playersSet.values, metric='euclidean'))[playerIndex])
    del distMatrix[playerIndex]
    del ids[playerIndex]
    replacementIndex = distMatrix.index(min(distMatrix))
    print("player replacent is " +str(ids[replacementIndex]))
    return

def replacementInTeam(player, dataFrame, dataArray, dataAttributes):
    club = ""
    playerTeamMates = []
    ids = []

    for index, row in dataFrame.iterrows():
        if(row["ID"] == player):
            club = row['Club']
            break

    if club != "":
        for index, row in dataFrame.iterrows():
            if(row["Club"] == club):
                playerTeamMates.append(list(row))
                ids.append(row["ID"])

    playersSet = pd.DataFrame(playerTeamMates, columns=dataAttributes)
    chooseReplacementInSet(playersSet, ids, player)
    return 

def replacementInSet(player, dataFrame, dataArray, dataAttributes):
    playersArray = []
    num  = input ('Enter numbers of players: ')

    for i in range(int(num)):
        playersArray.append(input(int()))

    playersArray.append(player)
    playerTeamMates = []
    ids = []
    for index, row in dataFrame.iterrows():
        if(row["ID"] != player and row["ID"] in playersArray):
            playerTeamMates.append(list(row))
            ids.append(row["ID"])
         
    playersSet = pd.DataFrame(playerTeamMates, columns=dataAttributes)
    chooseReplacementInSet(playersSet, ids, player)
    return

def chooseReplacement():
    print("1. Choosing a replacement in the set of Players")
    print("2. Choosing a replacement within team")
    option = input("Enter your choice: ")
    print("------------------------------------------------------------------------------")
    player = int(input("Enter player to be replaced "))
        
    dataFrame = pickle.load(open("pickels/cleanedDataDataFramePickel",'rb'))
    dataArray = pickle.load(open("pickels/cleanedDataDataArrayPickel",'rb'))
    dataAttributes = pickle.load(open("pickels/cleanedDataDataAttributesPickel",'rb'))

    if option == 1:
        replacementInSet(player, dataFrame, dataArray, dataAttributes)
    else:
        replacementInTeam(player, dataFrame, dataArray, dataAttributes)

chooseReplacement()