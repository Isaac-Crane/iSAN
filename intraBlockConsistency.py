import numpy as np
from scipy import stats
from spearman import runSpearman
import random
blocks = []
for i in range(8):
    blocks.append([])
    for j in range(8):
        blocks[i].append(random.random())

#returns the average consistency across blocks with the average. takes the vectorized blocks
def testBlockConsistency(blocks):
    consistencySum = 0
    for i in range(len(blocks)):
        sum = []
        for l in range(len(blocks[0])):
            sum.append(0)
        for j in range(len(blocks)):
            if i!=j:
                    for k in range(len(blocks[j])):
                        sum[k] += blocks[j][k]
        average = []
        for m in range(len(sum)):
            average.append(sum[m]/(len(blocks)-1))
        consistencySum += runSpearman(np.array(average), np.array(blocks[i]))
    consistencyAverage = consistencySum/len(blocks)
    return consistencyAverage