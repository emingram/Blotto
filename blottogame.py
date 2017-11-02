def BlottoGame (strat1, strat2, n):
    #plays one blotto game among strategy vectors strat1 and strat2 of length n. returns score for strat1

    p1score = p2score = 0   #initializing scores
    assert len(strat1) == len(strat2)   #make sure strats are the same length

    for i in range(n):  #check each field and assign scores
        if strat1[i] > strat2[i]:
            p1score += 1.0
        elif strat1[i] < strat2[i]:
            p2score += 1.0
        else:
            p1score += 0.5
            p2score += 0.5
    return p1score      #return the score of the first strategy vector
