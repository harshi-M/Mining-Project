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

print(len(df))

train, test = train_test_split(df, test_size=0.2)
print(len(train))
print(len(test))
# attr =['Age', 'Overall', 'Potential', 'International Reputation']

#training model
polynomial_features= PolynomialFeatures(degree=4)
# xTrainList = train[attr].values
# yTainList = train['Value'].values
# trainFeature = polynomial_features.fit_transform(xTrainList)
# model = LinearRegression()
# model.fit(trainFeature, yTainList)

#model from pickel

attr = pickle.load(open("pickels/costAttributesWithoutOverall",'rb'))
model = pickle.load(open("pickels/costModelWithoutOverall",'rb'))
print(attr)
#testing model
xTestList = test[attr].values
yTestList = test['Value'].values
testFeature = polynomial_features.fit_transform(xTestList)
polyPred = model.predict(testFeature)

#error calculation
error = np.sqrt(mean_squared_error(yTestList,polyPred))
print(error)