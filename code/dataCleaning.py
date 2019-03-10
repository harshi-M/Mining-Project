import pandas as pd

def readFile(fileName):
    #final array of data
    dataArray = []

    #handeling the encoding of the csv file and storing the data in lines var
    with open(fileName, 'rb') as fileContents:
        lines = [x.decode('utf8').strip() for x in fileContents.readlines()]

    #list of data attribute added extra column for form
    dataAttributes = ['ID', 'Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Value', 'Wage', 'Special', 'Preferred Foot', 'International Reputation', 'Weak Foot', 'Skill Moves', 'Work Rate', 'Body Type', 'Real Face', 'Position', 'Jersey Number', 'Joined', 'Loaned From', 'Contract Valid Until', 'Height', 'Weight', 'Form', 'LS', 'ST', 'RS','LW','LF','CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB','CB','RCB','RB', 'Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause']
    print(len(dataAttributes))
    #data type of each data attribute in the form of dictionary
    dataAttributesDataType = {'ID': "float", 'Name':"string", 'Age':"float", 'Nationality':"string", 'Overall':"float", 'Potential':"float", 'Club':"string", 'Value':"float", 'Wage':"float", 'Special':"float", 'Preferred Foot':"string", 'International Reputation':"float", 'Weak Foot':"float", 'Skill Moves':"float", 'Work Rate':"string", 'Body Type':"string", 'Real Face':"string", 'Position':"string", 'Jersey Number':"float", 'Joined':"string", 'Loaned From':"string", 'Contract Valid Until':"string", 'Height':"float", 'Weight':"float", "Form": "float", 'LS':"float", 'ST':"float", 'RS':"float", 'LW':"float", 'LF':"float", 'CF':"float",'RF':"float", 'RW':"float",  'LAM':"float", 'CAM':"float", 'RAM':"float", 'LM':"float", 'LCM':"float", 'CM':"float", 'RCM':"float", 'RM':"float", 'LWB':"float", 'LDM':"float", 'CDM':"float", 'RDM':"float",'RWB':"float", 'LB':"float", 'LCB':"float", 'CB':"float", 'RCB':"float", 'RB':"float", 'Crossing':"float", 'Finishing':"float", 'HeadingAccuracy':"float", 'ShortPassing':"float", 'Volleys':"float", 'Dribbling':"float", 'Curve':"float", 'FKAccuracy':"float", 'LongPassing':"float", 'BallControl':"float", 'Acceleration':"float", 'SprintSpeed':"float", 'Agility':"float", 'Reactions':"float", 'Balance':"float", 'ShotPower':"float", 'Jumping':"float", 'Stamina':"float", 'Strength':"float", 'LongShots':"float", 'Aggression':"float", 'Interceptions':"float", 'Positioning':"float", 'Vision':"float", 'Penalties':"float", 'Composure':"float", 'Marking':"float", 'StandingTackle':"float", 'SlidingTackle':"float", 'GKDiving':"float", 'GKHandling':"float", 'GKKicking':"float", 'GKPositioning':"float", 'GKReflexes':"float", 'Release Clause':"float"}
    
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
                # the first if case is to handel LS and teh extra form column and others all the form is ignored. 
                # as they are same but just appended to teh data so creating new column for each form will create duplicate data.
                if dataAttributes[attributeIndex]  == "Form":
                    #if the value do not exist then -1 is defaulted
                    if len(ele.strip()) == 0:
                        dataRowArray.append(-1)
                        dataRowArray.append(-1)
                    elif len(ele.split('+')) == 2:
                        #this adds the cloumn in the form 
                        dataRowArray.append(float(ele.split('+')[1].strip()))
                        # this add the cloumn values to LS column
                        dataRowArray.append(float(ele.split('+')[0].strip()))
                    else:
                        print(ele)
                        break
                    attributeIndex +=1

                elif dataAttributes[attributeIndex]  in ['LS', 'ST', 'RS','LW','LF','CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB','CB','RCB','RB'] :
                    #if the value do not exist then -1 is defaulted
                    if len(ele.strip()) == 0:
                        dataRowArray.append(-1)
                    elif len(ele.split('+')) == 2:
                        dataRowArray.append(float(ele.split('+')[0].strip()))
                    else:
                        print(ele)
                        break
                
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
[dataArray, dataAttributes] = readFile("data/cleanedData.csv")

#consrt the array to pandas data frame
dataFrame = pd.DataFrame(dataArray, columns=dataAttributes)

#the below one prints the entire data frame in tabular for easy to check
print(dataFrame)

#this function shows the stats for the colums in data frame
# printStatsatics(dataFrame, dataAttributes)
