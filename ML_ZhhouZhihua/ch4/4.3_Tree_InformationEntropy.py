from math import log
import operator
import numpy as np
import pandas as pd

'''
Function:Computing shannon entropy of a given data set
Input:dataSet
'''
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

#create test dataset
def CreateDataSet():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

def spliteDateSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def splitContinuousDataSet(dataSet,axis,value,dir):
    retDataSet = []
    for featVec in dataSet:
        if dir == 0:
            if featVec[axis]>value:
                reducedFeatVec = featVec[:axis]
                reducedFeatVec.extend(featVec[axis+1:])
                retDataSet.append(reducedFeatVec)
        else:
            if featVec[axis] <= value:
                reducedFeatVec = featVec[:axis]
                reducedFeatVec = featVec[axis+1:]
                retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    bestSplitDict = {}
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        #处理连续型特征
        if type(featList[0]).__name__ == 'float' or type(featList[0]).__name__ == 'int':
            sortFeatList = sorted(featList)
            splitList = []
            for j in range(len(sortFeatList) - 1):
                splitList.append((sortFeatList[j] + sortFeatList[j+1])/2)
            slen = len(splitList)
            for j in range(slen):
                value = splitList[j]
                newEntropy = 0.0
                subDataSet0 = splitContinuousDataSet(dataSet, i, value, 0)
                subDataSet1 = splitContinuousDataSet(dataSet, i, value, 1)
                prob0 = len(subDataSet0)/float(len(dataSet))
                newEntropy += prob0 * calcShannonEnt(subDataSet0)
                prob1 = len(subDataSet1)/float(len(subDataSet1))
                newEntropy += prob1 * calcShannonEnt(subDataSet1)
                infoGain = baseEntropy - newEntropy
                if(infoGain > baseEntropy):
                    baseEntropy = infoGain
                    bestFeature = i
                    bestSplit = j
                    bestSplitDict[labels[i]] = splitList[bestSplit]
        else:
            uniqueVals = set(featList)#集合，去重
            newEntropy = 0.0
            for value in uniqueVals:
                subDataSet = spliteDateSet(dataSet, i, value)
                prob = len(subDataSet)/float(len(dataSet))
                newEntropy += prob * calcShannonEnt(subDataSet)
            infoGain = baseEntropy - newEntropy
            if (infoGain > bestInfoGain):
                bestInfoGain = infoGain
                bestFeature = i
    if type(dataSet[0][bestFeature]).__name__=='float' or type(dataSet[0][bestFeature]).__name__=='int':
        bestSplitValue = bestSplitDict[labels[bestFeature]]
        labels[bestFeature]=labels[bestFeature]+'<='+str(bestSplitValue)
        for data in dataSet:
            if data[bestFeature] <= bestSplitValue:
                data[bestFeature]=1
            else:
                data[bestFeature]=0
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    #遍历完属性选择便签最多的类
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel : {}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(spliteDateSet(dataSet, bestFeat, value), subLabels)
    return myTree



if __name__ == '__main__':

    filePath = './watermelonDataSet3.0.csv'
    df = pd.read_csv(filePath)
    dataSet = df.values[:,1:].tolist()
    labels = df.columns.values[1:-1].tolist()
    myTree = createTree(dataSet,labels)
    print(myTree)

