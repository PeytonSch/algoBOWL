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


def algorithm_one(inputLines,m_clauses,n_variables,firstSolution):

    maxFromTrial = 0
    bestSatAmount = 0
    best_solution = []

    for i in range(1000):
        trial_solution = getLocalMaxForSolution(inputLines,m_clauses,n_variables,firstSolution,100)
        maxFromTrial = clausesSatisfied(trial_solution,inputLines)
        if(bestSatAmount < maxFromTrial):
            #print("Old Best was ",bestSatAmount," with: \n", trial_solution, "\n we get ", maxFromTrial, "\n")
            bestSatAmount = maxFromTrial
            best_solution = trial_solution
            print(bestSatAmount)
            #print("Best Solution is now \n", best_solution)
            #print("From jerry's algorithm this gives ", clausesSatisfied(best_solution,inputLines) )
            #print("\n\n********\n\n")
            #generateOutputToFile(clausesSatisfied(best_solution,inputLines),best_solution)

        for i in range(len(firstSolution)):
            firstSolution[i] = random.randint(0,1)

    print("Max Sat Amount: ", bestSatAmount)
    #print(best_solution)
    #print(clausesSatisfied(best_solution,inputLines))

    #generateOutputToFile(clausesSatisfied(best_solution,inputLines),best_solution)
