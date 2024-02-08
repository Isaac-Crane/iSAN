import numpy as np
def convertMatrixToUpperTriangleVector(matrix):
    npMatrix = np.array(matrix)
    vector = npMatrix[np.triu_indices(len(matrix), k = 1)]
    return vector