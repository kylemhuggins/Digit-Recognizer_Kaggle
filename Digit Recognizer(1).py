
# coding: utf-8

# In[46]:

# This is the Digit Recognizer submission for Krybaby_7_9

# A digit is made by a 28x28 pixel image; i.e., 784 total data points

import numpy as np
from collections import Counter
import csv


# In[47]:

# This section imports and shapes the train data

trainData = open("train-1.csv", "r")
readTrainData = trainData.read()
listTrainData = readTrainData.split("\n")
del listTrainData[0]
mTrain = len(listTrainData)

trainLabels = []
trainDigitSeries = []

for x in range(mTrain):
    newList2 = []
    
    string = listTrainData[x]
    trainLabels.append(string[0])
    series = string[2:]
    newList = series.split(",")
    
    for y in newList:
        integer = int(y)
        newList2.append(integer)
        
    trainDigitSeries.append(newList2)


# In[48]:

# This section imports and shapes the test data

testData = open("test.csv", "r")
readTestData = testData.read()
listTestData = readTestData.split("\n")
del listTestData[0]
mTest = len(listTestData)

testLabelsIdentified = []
testDigitSeries = []

for x in range(mTest):
    newList2 = []
    
    string = listTestData[x]
    newList = string.split(',')
    
    for y in newList:
        integer = int(y)
        newList2.append(integer)
    
    testDigitSeries.append(newList2)


# In[49]:

# This section creates does the fancy math

lengthTest = len(testDigitSeries)
lengthTrain = len(trainDigitSeries)
# len for both the shaped train and test sets should be the same
# THIS MIGHT NOT BE TRUE WHEN DATA SETS AREN'T TRUNCATED; BELIEVE IT'S 40,000 and 28,000

kValue = 5

for x in range(lengthTest):
    distances = []
    differenceList = []
    
    testScrutiny = testDigitSeries[x]
    
    for y in range(lengthTrain):
        trainScrutiny = trainDigitSeries[y]
        
        for z in range(784):
            difference = testScrutiny[z] - trainScrutiny[z]
            squared = difference**2
            differenceList.append(squared)
    
        summed = sum(differenceList)
        squareroot = summed**0.5
        distances.append(squareroot)
        
    together = zip(distances,trainLabels)
    sortedTogether = sorted(together)
    
    newDistances = [x[0] for x in sortedTogether]
    newTrainLabels = [x[1] for x in sortedTogether]
    
    identityList = newTrainLabels[0:kValue]
    theCounted = Counter(identityList)
    winner = theCounted.most_common(1)
    testLabelsIdentified.append(winner)


# In[51]:

o = len(testLabelsIdentified)
testInt = 1

with open("KrybabyDigits.csv", "w", newline='') as csvfile:
    digitWriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    digitWriter.writerow(["ImageId", "Label"])
    
    for x in range(o):
        digitWriter.writerow([testInt,testLabelsIdentified[x]])
        testInt += 1


# In[53]:

testLabelsIdentified
# THIS IS SO WRONG....
# Going to have to debug... likely in the fancy math section...


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



