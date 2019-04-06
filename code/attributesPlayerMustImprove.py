import dataCleaning as data
import cluster as cluster
import matplotlib.pyplot as plt
import pickle
import numpy as np

def attributesAboveThreshold(pos, threshold, dataFrame, dataAttributes):
    importantColums = []
    corealtionMatrix = dataFrame.corr()
    dataColumn = list(corealtionMatrix.loc[: , pos])
    index = 0
    for  row in dataColumn:
        if row > threshold:
            importantColums.append(dataAttributes[index])
        index += 1
    print(importantColums)
    return importantColums
    # if row['B'] > 1.5:
    #     calc_temp   = row['A'] *10
    #     calc_temp01 = row['C'] *-10


    
dataFrame = pickle.load(open("pickels/cleanedDataDataFramePickel",'rb'))
dataArray = pickle.load(open("pickels/cleanedDataDataArrayPickel",'rb'))
dataAttributes = pickle.load(open("pickels/cleanedDataDataAttributesPickel",'rb'))
# player = input("enter playerID")
expectedPos = input("enter expected pos")
threshold= 0.8
impAttributes = attributesAboveThreshold(expectedPos, threshold, dataFrame, dataAttributes)