import pandas as pd

def readFile(fileName):
    #final array of data
    dataArray = []

    #handeling the encoding of the csv file and storing the data in lines var
    with open(fileName, 'rb') as fileContents:
        lines = [x.decode('utf8').strip() for x in fileContents.readlines()]

    # dataAttributes = lines[0].strip().split(",")[1:]
    #list of data attribute added extra clums for form
    dataAttributes = ['ID', 'Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Value', 'Wage', 'Special', 'Preferred Foot', 'International Reputation', 'Weak Foot', 'Skill Moves', 'Work Rate', 'Body Type', 'Real Face', 'Position', 'Jersey Number', 'Joined', 'Loaned From', 'Contract Valid Until', 'Height', 'Weight', 'LS', 'LS-Form', 'ST', 'ST-Form', 'RS', 'RS-Form','LW', 'LW-Form','LF', 'LF-Form','CF', 'CF-Form','RF','RF-Form', 'RW', 'RW-Form', 'LAM','LAM-Form', 'CAM','CAM-Form', 'RAM','RAM-Form', 'LM','LM-Form', 'LCM','LCM-Form', 'CM','CM-Form', 'RCM','RCM-Form', 'RM','RM-Form', 'LWB','LWB-Form', 'LDM','LDM-Form', 'CDM','CDM-Form', 'RDM','RDM-Form', 'RWB','RWB-Form', 'LB','LB-Form', 'LCB','LCB-Form', 'CB','CB-Form', 'RCB','RCB-Form', 'RB','RB-Form', 'Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause']
    #data type of each data attribute in the form of dictionary
    dataAttributesDataType = {'ID': "float", 'Name':"string", 'Age':"float", 'Nationality':"string", 'Overall':"float", 'Potential':"float", 'Club':"string", 'Value':"float", 'Wage':"float", 'Special':"float", 'Preferred Foot':"string", 'International Reputation':"float", 'Weak Foot':"float", 'Skill Moves':"float", 'Work Rate':"string", 'Body Type':"string", 'Real Face':"string", 'Position':"string", 'Jersey Number':"float", 'Joined':"string", 'Loaned From':"string", 'Contract Valid Until':"string", 'Height':"float", 'Weight':"float", 'LS':"float", 'LS-Form':"float", 'ST':"float", 'ST-Form':"float", 'RS':"float", 'RS-Form':"float",'LW':"float", 'LW-Form':"float",'LF':"float", 'LF-Form':"float",'CF':"float", 'CF-Form':"float",'RF':"float",'RF-Form':"float", 'RW':"float", 'RW-Form':"float", 'LAM':"float",'LAM-Form':"float", 'CAM':"float",'CAM-Form':"float", 'RAM':"float",'RAM-Form':"float", 'LM':"float",'LM-Form':"float", 'LCM':"float",'LCM-Form':"float", 'CM':"float",'CM-Form':"float", 'RCM':"float",'RCM-Form':"float", 'RM':"float",'RM-Form':"float", 'LWB':"float",'LWB-Form':"float", 'LDM':"float",'LDM-Form':"float", 'CDM':"float",'CDM-Form':"float", 'RDM':"float",'RDM-Form':"float", 'RWB':"float",'RWB-Form':"float", 'LB':"float",'LB-Form':"float", 'LCB':"float",'LCB-Form':"float", 'CB':"float",'CB-Form':"float", 'RCB':"float",'RCB-Form':"float", 'RB':"float",'RB-Form':"float", 'Crossing':"float", 'Finishing':"float", 'HeadingAccuracy':"float", 'ShortPassing':"float", 'Volleys':"float", 'Dribbling':"float", 'Curve':"float", 'FKAccuracy':"float", 'LongPassing':"float", 'BallControl':"float", 'Acceleration':"float", 'SprintSpeed':"float", 'Agility':"float", 'Reactions':"float", 'Balance':"float", 'ShotPower':"float", 'Jumping':"float", 'Stamina':"float", 'Strength':"float", 'LongShots':"float", 'Aggression':"float", 'Interceptions':"float", 'Positioning':"float", 'Vision':"float", 'Penalties':"float", 'Composure':"float", 'Marking':"float", 'StandingTackle':"float", 'SlidingTackle':"float", 'GKDiving':"float", 'GKHandling':"float", 'GKKicking':"float", 'GKPositioning':"float", 'GKReflexes':"float", 'Release Clause':"float"}

    #reading line by line of csv and cleaning and keeping in required format
    for ipLine in lines[1:]:

        dataRowArray = []

        #helps to keep track which data attribute we are cosidering
        attributeIndex = 0

        #split the input csv (coma seperated values) based on ','
        for ele in ipLine.strip().split(",")[1:]:

            #check which data attribute we are considering and convert it into the format according to the dictionary that is created
            if dataAttributesDataType[dataAttributes[attributeIndex]] == "string":

                #if the foramt is string and the value id empty we are substituting with the none value else just append it as the vaues is already in string type
                if(len(ele.strip()) == 0 ):
                    dataRowArray.append(None)
                else:
                    dataRowArray.append(ele.strip())

            #if the data is float then....
            elif dataAttributesDataType[dataAttributes[attributeIndex]] == "float":

                #the first if case is to handel the ST	RS	LW	LF	CF	RF	RW	LAM	CAM and their form kinda shitty code but works 
                if attributeIndex+1 < len(dataAttributes) and  len(dataAttributes[attributeIndex+1].split("-")) == 2 :
                    if dataAttributes[attributeIndex +1].split("-")[1].strip() =='Form':
                        if len(ele.strip()) == 0:
                            #if the value do not exist then -1 is defaulted
                            dataRowArray.append(-1)
                            dataRowArray.append(-1)
                        elif len(ele.split('+')) == 2:
                            dataRowArray.append(float(ele.split('+')[0].strip()))
                            dataRowArray.append(float(ele.split('+')[1].strip()))
                        else:
                            print(ele)
                            break
                        attributeIndex += 1
                
                #if the value do not exist then -1 is defaulted
                elif(len(ele.strip()) == 0):
                    dataRowArray.append(-1)
                
                #if the column is height then convert it from feet to inches
                elif(dataAttributes[attributeIndex] == "Height"):
                    dataRowArray.append(float(ele.replace("'", "."))*12)
                
                #some money is in (string eds with K or M) K and M K = thousand and M - million so convert to int and multiply
                elif(ele.strip()[-1] == 'K'):
                    dataRowArray.append(float(ele.strip()[:-1])*1000)
                elif(ele.strip()[-1] == 'M'):
                    dataRowArray.append(float(ele.strip()[:-1])*1000000)

                #else just conevrt to float
                else:
                    dataRowArray.append(float(ele.strip()))

            else:
                #if this is hit somethig went wrong but it is not hit in this data set 
                #so hopefully this peice of code is working as expected fingers crossed
                print(dataAttributes[attributeIndex])
                print(ele)
                break
            
            #next data attribute in the single data line
            attributeIndex += 1

        #append the cleaned data line to op array
        dataArray.append(dataRowArray)

    return [dataArray, dataAttributes]

def printStatsatics(dataFrame, dataAttributes):
    print("data statastics")

    #consider each attribute and describe it vola dataframes does its magic :P
    for attribute in dataAttributes:
        print(dataFrame[attribute].describe())

        print("-------------------")
    print("######################")
    return

#cleanedData.csv the celaned data
#sampleData.csv just 4 rows maily for testing
[dataArray, dataAttributes] = readFile("sampleData.csv")

#consrt the array to pandas data frame
dataFrame = pd.DataFrame(dataArray, columns=dataAttributes)

#the below one prints the entire data frame in tabular for easy to check
print(dataFrame.to_string())

#this function shows the stats for the colums in data frame
# printStatsatics(dataFrame, dataAttributes)
