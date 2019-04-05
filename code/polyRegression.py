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


train, test = train_test_split(df, test_size=0.2)

allAtrr = ['Age', 'Overall', 'Potential', 'Special','International Reputation', 'Skill Moves', 'ShortPassing','LongPassing', 'BallControl','Reactions', 'Vision', 'Composure']
minVAL = -1
minCombo = []
for i in range(len(allAtrr)):
    attrList = list(combinations(allAtrr, i + 1))
    for x in attrList:
        
        attr = list(x)
        
        polynomial_features= PolynomialFeatures(degree=4)
        
        xList = df[attr].values
        yList = df['Value'].values
        x_poly = polynomial_features.fit_transform(xList)
        
        model = LinearRegression()
        model.fit(x_poly, yList)
        
        y_poly_pred = model.predict(x_poly))
        error = np.sqrt(mean_squared_error(yList,y_poly_pred))
        print(error)
        if minVAL == -1 or minVAL > error:
            minVAL = error
            minCombo = attr
print("----------------------------")
print(minVAL)
print(minCombo)