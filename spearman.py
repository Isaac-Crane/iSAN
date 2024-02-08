import numpy as np
from scipy import stats

def runSpearman(x, y):
    res = stats.spearmanr(x, y)
    return res.statistic