import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from itertools import combinations
import numpy as np
# -*- coding: utf-8 -*-

df = pickle.load(open("cleanedDataDataFramePickel",'rb'))
dataArray = pickle.load(open("cleanedDataDataArrayPickel",'rb'))
dataAttributes = pickle.load(open("cleanedDataDataAttributesPickel",'rb'))


train, test = train_test_split(df, test_size=0.02)

allAtrr = ['Age', 'Overall', 'Reactions', 'ShortPassing','LongPassing', 'Vision', 'Composure']
minVAL = -1
minCoeff = -1
minCombo = []
for i in range(len(allAtrr)):
    attrList = list(combinations(allAtrr, i + 1))
    for x in attrList:
        attr = list(x)        
        polynomial_features= PolynomialFeatures(degree=5)
        xTrainList = train[attr].values
        yTainList = train['Potential'].values
        trainFeature = polynomial_features.fit_transform(xTrainList)
        model = LinearRegression()
        model.fit(trainFeature, yTainList)

        #testing model
        xTestList = test[attr].values
        yTestList = test['Potential'].values
        testFeature = polynomial_features.fit_transform(xTestList)
        polyPred = model.predict(testFeature)
        
        error = np.sqrt(mean_squared_error(yTestList,polyPred))
        print(error)
        if minVAL == -1 or minVAL > error:
            minVAL = error
            minCombo = attr
            minCoeff = model.coef_
print("----------------------------")
print(minVAL)
print(minCombo)
print(minCoeff)
# 6381240104.69675 - ['Overall','International Reputation', 'Potential']
#  9296623193.713446 - 


#536743.7611382051
#['Age', 'Overall', 'Potential', 'International Reputation', 'Skill Moves', 'ShortPassing', 'LongPassing', 'BallControl', 'Vision']