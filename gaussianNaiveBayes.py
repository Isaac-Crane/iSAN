from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import numpy as np
import random
X = []
y = []
for i in range(100):
    vector = []
    for j in range(100):
        if i%2 == 0:
            value = 1-(random.random()/2)
        else:
            value = random.random()
        vector.append(value)
    X.append(vector)
    y.append(i%2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print(y_pred)

X_test = np.array(X_test)
print("Number of mislabeled points out of a total", str(X_test.shape[0]), "points:", str((y_test != y_pred).sum()))
print(gnb.predict_joint_log_proba(X))
X = np.array(X)
print(X.shape)