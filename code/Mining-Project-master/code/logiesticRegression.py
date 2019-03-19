import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from itertools import combinations
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
        print(attr)
        reg = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(df[attr], df['Value'])
        #print(reg.coef_)
        #print(reg.intercept_)
        
        predictions = list(reg.predict(test[attr]))
        expected = list(test['Value'])
        error = 0
        for rowIndex in range(len(predictions)):
            #print(str(predictions[rowIndex])+ " - " + str(expected[rowIndex])) 
            error += abs(predictions[rowIndex] - expected[rowIndex])
        print(error)
        if minVAL == -1 or minVAL > error:
            minVAL = error
            minCombo = attr
print("----------------------------")
print(minVAL)
print(minCombo)
# 6381240104.69675 - ['Overall','International Reputation', 'Potential']
#  9296623193.713446 - 