from util.generateOutput import *


def runExhaustiveAlgorithm(inputList,allTfCombinations,m_clauses,n_variables):

    maxNumberOfClausesSatisfied = 0
    bestOutput = []


    #test each combination of tf values
    for combination in allTfCombinations:
        combinationTrueCount = 0
        #with each combination go through input list and evaluate each clause
        for clause in inputList:
            #each clause is [#, #]
            if(int(clause[0]) > 0 and int(clause[1]) > 0):
                #both clauses are as is
                result = combination[0] or combination[1]
            elif(int(clause[0]) < 0 and int(clause[1]) < 0):
                #both clauses are not
                result = not combination[0] or not combination[1]
            elif(int(clause[0]) > 0 and int(clause[1]) < 0):
                #2nd clause is not
                result = combination[0] or not combination[1]
            elif(int(clause[0]) < 0 and int(clause [1]) > 0):
                #first clause is not
                result = not combination[0] or combination[1]

            if result is True:
                combinationTrueCount = combinationTrueCount + 1

        if combinationTrueCount >= maxNumberOfClausesSatisfied:
            maxNumberOfClausesSatisfied = combinationTrueCount
            bestOutput = combination


    print(best)
    generateOutputToConsole(maxNumberOfClausesSatisfied,bestOutput)

    generateOutputToFile(maxNumberOfClausesSatisfied,bestOutput)
