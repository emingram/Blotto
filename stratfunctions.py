import numpy as np

def RandoStrat (init, n): #this function makes very skew distributions
    #create a single random integer-valued strategy that sums to init with length n
    res = init      #create a temporary resource variable
    strat = []      #empty list
    for i in range(n-1):
        rand = np.random.randint(0, res)    #fill each position in the vector with a random int from 0 to the remaining reserves
        strat.append(rand)
        res -= rand         #reduce reserves by this number
    strat.append(rand)      #add this to the strategy vector
    np.random.shuffle(strat)   #shuffle the strategy vector
    return strat

def RandoDist (init, n, x): #this function makes very uniform distributions
    #creates a strategy that adds x units of resources to a random district
    strat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while sum(strat)<init:
        dist = np.random.randint(0, n)  #choose a district randomly
        strat[dist] += x    #add 5 resources to that district
    return strat


