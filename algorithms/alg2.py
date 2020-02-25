from util.clausesSatisfied import *
from util.generateOutput import *
import random

import time

def getNextSolution(inputLines,m_clauses,n_variables,firstSolution,runNumber,currentMax,best_solution):
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


    runNumber = runNumber -1

    #still working to local max
    if (not(change_to == -1)):
        firstSolution[steepest_index] = change_to
        ###
        print("The steepest index is ",steepest_index,"with nothing changed we get ", original_sat, " with this we get ", maxNumberOfClausesSatisfied)
        if runNumber <= 0:
            print("Number of iterations used up, returning where we are at")
            return best_solution
        else:
            return getNextSolution(inputLines,m_clauses,n_variables,firstSolution,runNumber,currentMax,best_solution)

    #local found
    else:
        if maxNumberOfClausesSatisfied > currentMax:
            best_solution = firstSolution
        if runNumber <= 0:
            print("Number of iterations used up, returning where we are at")
            return best_solution
        print("Change to is -1, this must mean we are at a local max? Picking new start point")
        print("The steepest index is ",steepest_index,"with nothing changed we get ", original_sat, " with this we get ", maxNumberOfClausesSatisfied)

        #return firstSolution
        print("NEW RANDOM 1")
        for i in firstSolution:
            i = random.randint(0,1)
        return getNextSolution(inputLines,m_clauses,n_variables,firstSolution,runNumber,currentMax,best_solution)




def algorithm_one(inputLines,m_clauses,n_variables,firstSolution):

    best_solution = firstSolution
    currentMax = clausesSatisfied(firstSolution,inputLines)

    start = time.time()
    total_best_solution = getNextSolution(inputLines,m_clauses,n_variables,firstSolution,100,currentMax,best_solution)
    print(time.time()-start)

    generateOutputToFile(clausesSatisfied(total_best_solution,inputLines),total_best_solution)
