import pickle
import itertools
import whatAttributesToImprove as attrImprove

formationsList = [ [4, 4, 2], [4,3,3], [4,4,2], [4, 3, 2, 1], [5, 3, 2], [3, 4, 3], [3, 5, 2], [3, 4, 1, 2], [3, 6, 1], [4, 5, 1], [4, 2, 3, 1], [4, 6,0], [5, 4, 1], [1, 6, 3], [4, 2, 2, 2], [3, 3, 1, 3], [3, 3, 3, 1], [4, 2, 1, 3]]
allPossiblePositions = ['RB','RW','CM','LAM','ST','CB','LCM','RCB','CAM','RWB','GK','RS','RM','CDM','LB','LF','RAM','LWB','RF','RDM','RCM','LM','LS','LDM','LCB','LW','CF']
formationsPositions = [
    #['RB','RW','CM','LAM','ST','CB','LCM','RCB','CAM','RWB','GK','RS','RM',
    # 'CDM','LB','LF','RAM','LWB','RF','RDM','RCM','LM','LS','LDM','LCB','LW','CF']
    ['LF', 'RF', 'CAM', 'RM', 'LM', 'CDM', 'LB', 'RB', 'LCB', 'RCB'], #[4, 4, 2]
    ['CF', 'LW', 'RW', 'RCM', 'LCM', 'CM', 'LWB', 'LB', 'RB', 'RWB'], #[4,3,3]
    ['LS', 'RS', 'LM', 'RM', 'CAM', 'CDM', 'LWB', 'LB', 'RB', 'RWB'], #[4,4,3]
    ['CF', 'CAM', 'LM', 'RM', 'LDM', 'RDM', 'LWB', 'LB', 'RB', 'RWB'], #[4,4,1,1]
    ['ST', 'LAM', 'RAM', 'RM', 'LM', 'CM', 'LWB', 'LB', 'RB', 'RWB'], #[4,3,2,1]
    ['LS', 'RS', 'LM', 'RM', 'CM', 'LWB', 'LB', 'CB', 'RB', 'RWB'] #[5,3,2]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[4,4,2]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[4, 3, 2, 1]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[5, 3, 2] 
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[3, 4, 3]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[3, 5, 2]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[3, 4, 1, 2]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[3, 6, 1]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[4, 5, 1]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[4, 2, 3, 1]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[4, 6,0]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[5, 4, 1]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[1, 6, 3]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[4, 2, 2, 2]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[3, 3, 1, 3]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[3, 3, 3, 1]
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #[4, 2, 1, 3]
]


def getDetails():
    playersPosition = {}

    for formation in formationsList:
        print(str(formationsList.index(formation) + 1), " : ", "-".join([str(x) for x in formation]))

    formation = int(input("Choose the formation that must be formed with the players"))-1
    print("Formation choosen = ", str(formationsList[formation]))
    
    for position in formationsPositions[formation]:
        print("Enter player to play in position ", position)
        playerId = int(input())
        playersPosition[position] = playerId
        if(playerId<= 0):
            print("invalid entry")
            exit(0)
    return [playersPosition, formation]

[playersPosition, formation] = getDetails()
for position in playersPosition.keys():
    attrImprove.getClosestInClusters(position, playersPosition[position])