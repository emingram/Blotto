import numpy as np

def RandoStrat (init, n):
    #create a single random integer-valued strategy that sums to init with length n
    res = init      #create a temporary resource variable
    strat = []      #empty list
    for i in range(n-1):
        rand = np.random.randint(0, res)    #fill each position in the vector with a random int from 0 to the remaining reserves
        strat.append(rand)
        res -= rand         #reduce reserves by this number
    strat.append(rand)      #add this to the strategy vector
    random.shuffle(strat)   #shuffle the strategy vector
    return strat

