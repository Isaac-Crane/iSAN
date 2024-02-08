import numpy as np
from scipy import stats

def runPearson(x, y):
    res = stats.pearsonr(x, y)
    print(res.statistic)
    print(res.pvalue)
    return res.statistic