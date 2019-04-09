import pickle

formationsList = [ [4, 4, 2], [4,3,3], [4,4,2], [4, 3, 2, 1], [5, 3, 2], [3, 4, 3], [3, 5, 2], [3, 4, 1, 2], [3, 6, 1], [4, 5, 1], [4, 2, 3, 1], [4, 6, 0], [5, 4, 1], [1, 6, 3], [4, 2, 2, 2], [3, 3, 1, 3], [3, 3, 3, 1], [4, 2, 1, 3]]
for formation in formationsList:
    print(str(formationsList.index(formation) + 1), " : ", "-".join([str(x) for x in formation]))
formation = int(input("Choose the formation that must be formed with the players"))-1
print("Formation choosen = ", str(formationsList[formation]))
playersCount = int(input("Enter number of players"))
if playersCount < 10:
    print("more players required")
    exit(0)
players= []
for player in range(playersCount):
    print("Enter player no", str(player+1))
    playerId = int(input())
    if(playerId<= 0):
        print("invalid entry")
        exit(0)
    players.append(playerId)
print(players)