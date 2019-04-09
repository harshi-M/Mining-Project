import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from itertools import combinations
import numpy as np


df = pickle.load(open("pickels/cleanedDataFramePickel",'rb'))
dataArray = pickle.load(open("pickels/cleanedDataArrayPickel",'rb'))
dataAttributes = pickle.load(open("pickels/cleanedDataAttributesPickel",'rb'))

train, test = train_test_split(df, test_size=0.2)

allAtrr = ['Age', 'Overall', 'Potential', 'Special','International Reputation', 'Skill Moves', 'ShortPassing','LongPassing', 'BallControl','Reactions', 'Vision', 'Composure', 'LS', 'ST', 'RS','LW','LF','CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB','CB','RCB','RB']
minVAL = -1
minCombo = []
for i in range(len(allAtrr)):
    attrList = list(combinations(allAtrr, i + 1))
    for x in attrList:
        
        attr = list(x)
        
        polynomial_features= PolynomialFeatures(degree=4)
        xTrainList = train[attr].values
        yTainList = train['Value'].values
        trainFeature = polynomial_features.fit_transform(xTrainList)
        model = LinearRegression()
        model.fit(trainFeature, yTainList)

        #testing model
        xTestList = test[attr].values
        yTestList = test['Value'].values
        testFeature = polynomial_features.fit_transform(xTestList)
        polyPred = model.predict(testFeature)
        
        error = np.sqrt(mean_squared_error(yTestList,polyPred))
        print(error)
        if minVAL == -1 or minVAL > error:
            minVAL = error
            minCombo = attr
            pickle.dump(attr, open("pickels/costAttributesWithoutOverall",'wb'))
            pickle.dump(model, open("pickels/costModelWithoutOverall",'wb'))
print("----------------------------")
print(minVAL)
print(minCombo)