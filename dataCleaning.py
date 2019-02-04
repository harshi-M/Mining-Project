def readFile(fileName):
    dataArray = []
    with open(fileName, 'rb') as fileContents:
        lines = [x.decode('utf8').strip() for x in fileContents.readlines()]
    dataAttributes = lines[0].strip().split(",")[1:]
    dataAttributesDataType = {'ID': "float", 'Name':"string", 'Age':"float", 'Nationality':"string", 'Overall':"float", 'Potential':"float", 'Club':"string", 'Value':"float", 'Wage':"float", 'Special':"float", 'Preferred Foot':"string", 'International Reputation':"float", 'Weak Foot':"float", 'Skill Moves':"float", 'Work Rate':"string", 'Body Type':"string", 'Real Face':"string", 'Position':"string", 'Jersey Number':"float", 'Joined':"string", 'Loaned From':"string", 'Contract Valid Until':"string", 'Height':"float", 'Weight':"float", 'LS':"string", 'ST':"string", 'RS':"string", 'LW':"string", 'LF':"string", 'CF':"string", 'RF':"string", 'RW':"string", 'LAM':"string", 'CAM':"string", 'RAM':"string", 'LM':"string", 'LCM':"string", 'CM':"string", 'RCM':"string", 'RM':"string", 'LWB':"string", 'LDM':"string", 'CDM':"string", 'RDM':"string", 'RWB':"string", 'LB':"string", 'LCB':"string", 'CB':"string", 'RCB':"string", 'RB':"string", 'Crossing':"float", 'Finishing':"float", 'HeadingAccuracy':"float", 'ShortPassing':"float", 'Volleys':"float", 'Dribbling':"float", 'Curve':"float", 'FKAccuracy':"float", 'LongPassing':"float", 'BallControl':"float", 'Acceleration':"float", 'SprintSpeed':"float", 'Agility':"float", 'Reactions':"float", 'Balance':"float", 'ShotPower':"float", 'Jumping':"float", 'Stamina':"float", 'Strength':"float", 'LongShots':"float", 'Aggression':"float", 'Interceptions':"float", 'Positioning':"float", 'Vision':"float", 'Penalties':"float", 'Composure':"float", 'Marking':"float", 'StandingTackle':"float", 'SlidingTackle':"float", 'GKDiving':"float", 'GKHandling':"float", 'GKKicking':"float", 'GKPositioning':"float", 'GKReflexes':"float", 'Release Clause':"float"}
    for ipLine in lines[1:]:
        dataRowArray = []
        attributeIndex = 0
        for ele in ipLine.strip().split(",")[1:]:
            if dataAttributesDataType[dataAttributes[attributeIndex]] == "string":
                if(len(ele.strip()) == 0 ):
                    dataRowArray.append(None)
                else:
                    dataRowArray.append(ele.strip())
            elif dataAttributesDataType[dataAttributes[attributeIndex]] == "float":
                if(len(ele.strip()) == 0):
                    dataRowArray.append(-1)
                elif(dataAttributes[attributeIndex] == "Height"):
                    dataRowArray.append(float(ele.replace("'", "."))*12)
                elif(ele.strip()[-1] == 'K'):
                    dataRowArray.append(float(ele.strip()[:-1])*1000)
                elif(ele.strip()[-1] == 'M'):
                    dataRowArray.append(float(ele.strip()[:-1])*1000000)
                else:
                    dataRowArray.append(float(ele.strip()))
            else:
                print(dataAttributes[attributeIndex])
                print(ele)
                break
            attributeIndex += 1
        dataArray.append(dataRowArray)
    print(dataArray[-1])
    return [dataArray, dataAttributes]

[dataArray, dataAttributes] = readFile("cleanedData.csv")
