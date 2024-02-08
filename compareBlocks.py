import numpy as np
from intraBlockConsistency import testBlockConsistency
import random
rest = []
task = []
restConsistency = testBlockConsistency(rest)
taskConsistency = testBlockConsistency(task)
all = []
for i in range(len(rest)):
    all.append(rest[i])
for i in range(len(task)):
    all.append(task[i])
allConsistency = testBlockConsistency(all)
print(restConsistency, taskConsistency, allConsistency)
print(len(task))