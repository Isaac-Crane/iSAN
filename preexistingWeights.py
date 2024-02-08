from sklearn import svm

def testBlock(blocks, test, testType):
    X = []
    y = []
    for i in range(len(blocks)):
        X.append(blocks[i][0])
        y.append(blocks[i][1])
    clf = svm.SVC(kernel='linear')
    clf.fit(X, y)
    if clf.predict([test]) == testType:
        return 1
    else:
        return 0
def getOverallWeights(blocks):
    X = []
    y = []
    for i in range(len(blocks)):
        X.append(blocks[i][0])
        y.append(blocks[i][1])
    clf = svm.SVC(kernel='linear')
    clf.fit(X, y)
    return clf.coef_


#blocks = [[vector, type]]
sum = 0
for i in range(len(blocks)):
    blocksSubset = []
    for j in range(len(blocks)):
        if j!=i:
            blocksSubset.append(blocks[j])
    sum+=testBlock(blocksSubset, blocks[i][0], blocks[i][1])
print(sum/len(blocks))
weights = getOverallWeights(blocks)
print(weights)