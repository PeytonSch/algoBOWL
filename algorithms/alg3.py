#
#Just randomly try combinations and save the best one
#

from util.clausesSatisfied import *
from util.generateOutput import *
import random

import time

def algorithm_three(inputLines,m_clauses,n_variables,firstSolution):

    maxFromTrial = 0
    bestSatAmount = 0
    best_solution = []

    for i in range(1000000):
        maxFromTrial = clausesSatisfied(firstSolution,inputLines)
        if(bestSatAmount < maxFromTrial):
            bestSatAmount = maxFromTrial
            best_solution = firstSolution
            print(bestSatAmount)

        for i in range(len(firstSolution)):
            firstSolution[i] = random.randint(0,1)

    print("Max Sat Amount: ", bestSatAmount)
