def splitDataSet(dataSet, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[0] == value:
            retDataSet.append(featVec[1:])
    return retDataSet


def get_rate(dataSet):
    sum = 0
    count = 0
    for featVec in dataSet:
        sum += 1
        if featVec[-1] == '1':
            count += 1
    rate = float(count) / float(sum)
    return round(rate, 2)


def createTree(dataSet):
    Rate = str(get_rate(dataSet))
    flag = 0.0
    count = 0.0
    for example in dataSet:
        for i in example[:-1]:
            count += 1
            if i != 0:
                flag += 1
    if len(dataSet[0]) == 1 or (flag/count) <= 0.01:
        return Rate
    myTree = {Rate: {}}
    featValues = [example[0] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        myTree[Rate][value] = createTree(splitDataSet(dataSet, value))
    return myTree


def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)


def predict(round_history, mytree, count, want):
    history = [example for example in round_history[:count]]
    dict = mytree
    predict = history[:]
    predict.append(want)
    for j in range(count + 1):
        value = predict[j]
        key = dict.keys()[0]
        dict = dict[key][value]
    return dict.keys()[0]
