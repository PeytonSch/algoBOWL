#
#Start with all trues, find local max
#then take random inputs and find local maxes on them
#

from util.clausesSatisfied import *
from util.generateOutput import *
import random

import time

def getLocalMaxForSolution(inputLines,m_clauses,n_variables,firstSolution,runNumber):
    maxNumberOfClausesSatisfied = clausesSatisfied(firstSolution,inputLines)
    original_sat = maxNumberOfClausesSatisfied

    steepest_index = -1
    change_to = -1

    for i in range(len(firstSolution)):
        if firstSolution[i] == 0:
            firstSolution[i] = 1
            case_number_satisfied = clausesSatisfied(firstSolution,inputLines)

            if case_number_satisfied > maxNumberOfClausesSatisfied:
                maxNumberOfClausesSatisfied = case_number_satisfied
                steepest_index = i
                change_to = 1
            firstSolution[i] = 0

        elif firstSolution[i] == 1:
            firstSolution[i] = 0
            case_number_satisfied = clausesSatisfied(firstSolution,inputLines)

            if case_number_satisfied > maxNumberOfClausesSatisfied:
                maxNumberOfClausesSatisfied = case_number_satisfied
                steepest_index = i
                change_to = 0
            firstSolution[i] = 1

    if (not(change_to == -1)):
        firstSolution[steepest_index] = change_to
    else:
        #print("Change to is -1, this must mean we are at a local max? ")
        #print("The steepest index is ",steepest_index,"with nothing changed we get ", original_sat, " with this we get ", maxNumberOfClausesSatisfied)
        return firstSolution

    #print("The steepest index is ",steepest_index,"with nothing changed we get ", original_sat, " with this we get ", maxNumberOfClausesSatisfied)
    runNumber = runNumber -1
    if runNumber == 0:
        #print("Number of iterations used up, returning where we are at")
        return firstSolution
    else:
        return getLocalMaxForSolution(inputLines,m_clauses,n_variables,firstSolution,runNumber)


def algorithm_one(inputLines,m_clauses,n_variables,firstSolution,outputFiles,f):

    startTime = time.time()
    timeToRun = 1500

    maxFromTrial = 0
    bestSatAmount = 0
    best_solution = []

    for i in range(1000):
        if time.time() > (startTime+timeToRun):
            #print(time.time(), " > ", startTime, " + ", timeToRun, " -ran ", i , " times")
            break
        trial_solution = getLocalMaxForSolution(inputLines,m_clauses,n_variables,firstSolution,20)
        maxFromTrial = clausesSatisfied(trial_solution,inputLines)
        if(bestSatAmount < maxFromTrial):
            bestSatAmount = maxFromTrial
            best_solution = trial_solution
            print(bestSatAmount)

            generateOutputToFile(clausesSatisfied(best_solution,inputLines),best_solution,outputFiles[f])

        for i in range(len(firstSolution)):
            firstSolution[i] = random.randint(0,1)

    print("Time:  ", time.time()-startTime)
