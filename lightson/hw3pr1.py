#
# Lights out in 1D
#

import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.
import sys            # larger recursive stack
sys.setrecursionlimit(10000) # 10000 stack frames availble

def timesTwo(i, oldL):
    """ Accepts an index (i) and an old list (oldL).

    """
    new_ith_element = 2 * oldL[i]
    return new_ith_element

def sqr(i, oldL):
    """Accepts an index (i) and an old list (oldL).
    """
    new_ith_element = oldL[i]*oldL[i]
    return new_ith_element

def rot(i, oldL):
    """"Accepts an index (i) and an old list (oldL).
    """
    new_ith_element = oldL[i - 1]
    return new_ith_element

def rand(i, oldL):
    """"Accepts an index (i) and an old list (oldL).
    """
    new_ith_element = choice([0, 1])
    return new_ith_element


def allOnes(L):
    """"Accepts a list and checks if it only contains 1's. If it does
    it returns true.
    """
    #for i in L:
    #    if L[i] != 1:
    #        return False
    #    else:
    #        return True
    if L == []:
        return True
    else:
        if L[0] != 1:
            return False
        else:
            return allOnes(L[1:])

    

def mutate(i, oldL):
    """ Accepts an index (i) and an old list (oldL).
        mutate returns the ith element of a NEW list!
        * Note that mutate returns ONLY the ith element
          mutate thus needs to be called many times in evolve.
    """
    new_ith_element = 1 + oldL[i]
    return new_ith_element

def randBL(N):
    """take in a nonnegative integer, N and 
    should return a list of length N, in 
    which each element is randomly either a 0 or a 1.
    """
    #return [ choice([0,1]) ] * N   # won't work!!
    tempList = []
    while N > 0:
        tempList.append(choice([0,1]))
        N -= 1
    return tempList

def easyIndex(N):
    """return a list that matches the index of the game index
    """
    tempList = []
    i = 0
    while i < N:
        tempList.append(i)
        i += 1
    return tempList


def toggle(i, oldL, target = 0):
    """ Accepts an index (i), an old list (oldL) and the index to turn on (target).
        turn_on_one returns the ith element of a NEW list!
        * Note that turn_on_one returns ONLY the ith element
          turn_on_one thus needs to be called many times in evolve.
    """
    if i == target or i == target + 1 or i == target - 1:
        new_ith_element = 1 - oldL[i]      # this makes the game easy!
    else:
        new_ith_element = oldL[i] # the new is the same as the old
    return new_ith_element


def evolve(oldL, mutate, curgen = 0):
    """ This function should evolve oldL (a list)
        it starts at curgen, the "current" generation
        and it ends at generation #5 (for now)
        
        It works by calling mutate at each index i.
    """
    print(easyIndex(len(oldL)))   # print a helper index above
    print(oldL, end='')                    # print the old list, L
    print("  (gen: " + str(curgen) + ")", end='')  # and its gen.
    time.sleep(0.25)
    
    #if curgen == 5:  # we're done!
    if allOnes(oldL):
        return curgen #return how many generations it took to get to all 1's
    else:
        user = int(input(" Index? "))
        newL = [ mutate(i,oldL,user) for i in range(len(oldL)) ]
        return evolve(newL, mutate, curgen + 1)

def evolveComputer(oldL, mutate, curgen = 0):
    """ This function should evolve oldL (a list)
        it starts at curgen, the "current" generation
        and it ends at generation #5 (for now)
        
        It works by calling mutate at each index i.
    """
    print(easyIndex(len(oldL)))   # print a helper index above
    print(oldL, end='')                    # print the old list, L
    print("  (gen: " + str(curgen) + ")")  # and its gen.
    time.sleep(0.25)
    
    #if curgen == 5:  # we're done!
    if allOnes(oldL):
        return curgen #return how many generations it took to get to all 1's
    else:
        user = int(choice(range(len(oldL))))
        newL = [ mutate(i,oldL,user) for i in range(len(oldL)) ]
        return evolveComputer(newL, mutate, curgen + 1)

#evolve( [0,0,0,0,1], rand )
#Should expect it to take around 10 generations
#evolve( [0,0,0,0,0,0,0,0], toggle )
#print(randBL(10))
#evolve(randBL(5), toggle)
evolveComputer(randBL(5), toggle)
