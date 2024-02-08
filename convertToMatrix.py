import numpy as np
def convertVectorToMatrix(vector, size):
    matrix = []
    upperIndex = 0
    lowerIndex = 0
    for j in range(size):
        matrix.append([])
        for k in range(size):
            if j == k:
                matrix[j].append(1)
            if k > j: 
                matrix[j].append(vector[upperIndex])
                upperIndex += 1
            if k < j: 
                matrix[j].append(vector[lowerIndex])
                lowerIndex += 1
    return matrix
size = 15
vector = []
for i in range(int(size*(size-1)*0.5)):
    vector.append(i+1)
convertVectorToMatrix(vector, size)