from sklearn.ensemble import GradientBoostingClassifier
import random
import numpy as np
rest = []
task = []
for i in range(1000):
    rest.append([])
    for j in range(8):
        rest[i].append(random.random())
for i in range(1000):
    task.append([])
    for j in range(8):
        task[i].append(random.random())
blocks = []
for i in range(len(rest)):
    blocks.append([rest[i], 'rest'])
for i in range(len(task)):
    blocks.append([task[i], 'task'])

for i in range(len(blocks)):
    train = blocks.copy()
    train.remove(blocks[i])
    X_train = []
    y_train = []
    for j in range(len(train)):
        X_train.append(blocks[j][0])
        y_train.append(blocks[j][1])
    X_test = blocks[i][0]
    y_test = blocks[i][1]
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)
    y_test = np.array(X_train)

    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(X_train, y_train)
    clf.score(X_test, y_test)