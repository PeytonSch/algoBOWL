import random

from util.clausesSatisfied import *

def runLocalMax(n_variable, bestSolution, clauses):

    currentPath = clausesSatisfied(bestSolution,clauses)
    solutions = []
    for i in bestSolution:
        if(int(i) == 0):
            i = 1
        else:
            i = 0
        solutions.append(clausesSatisfied(bestSolution,clauses))
        if (int(i) == 0):
            i = 1
        else:
            i = 0
    bestPathLength = max(solutions)
    bestChangeIndex = solutions.index(max(solutions))

    if bestSolution[bestChangeIndex] == 1:
        bestSolution[bestChangeIndex] = 0
    else:
        bestSolution[bestChangeIndex] = 1

    if(bestPathLength > currentPath):
        runLocalMax(n_variable,bestSolution,clauses)

    print(max(solutions))