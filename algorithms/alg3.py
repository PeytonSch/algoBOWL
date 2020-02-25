from util.clausesSatisfied import *
from util.generateOutput import *
import random

import time

def algorithm_three(inputLines,m_clauses,n_variables,firstSolution):

    maxFromTrial = 0
    bestSatAmount = 0
    best_solution = []

    for i in range(1000):
        maxFromTrial = clausesSatisfied(trial_solution,inputLines)
        if(bestSatAmount < maxFromTrial):
            bestSatAmount = maxFromTrial
            best_solution = trial_solution
            print(bestSatAmount)

        for i in range(len(firstSolution)):
            firstSolution[i] = random.randint(0,1)

    print("Max Sat Amount: ", bestSatAmount)
