#
#Take look at every single variable and see how many times they are true or false
#whichever is greater we set that as our ans value
#

from util.clausesSatisfied import *
from util.generateOutput import *
import random
from collections import Counter

import time


def rankInputsAlg2(inputLines,m_clauses,n_variables):



    allVariables = []

    finalAns = []

    for i in range(len(inputLines)):
        var1 = inputLines[i][0]
        var2 = inputLines[i][1]

        allVariables.append(var1)
        allVariables.append(var2)

    rankDict = Counter(allVariables)

    #print(rankDict.most_common(3))
    #print(rankDict[str(-310)])



    for i in range(int(n_variables)):
        value = str(i)
        negative = str(-i)

        if rankDict[value] <= rankDict[negative]:
            #print(rankDict[value], "is less than ", rankDict[negative], " so rankDict[value] will be false")
            finalAns.append(0)
        else:
            #print(rankDict[value], "is greater than ", rankDict[negative], " so rankDict[value] will be true")
            finalAns.append(1)

    print(clausesSatisfied(finalAns,inputLines))
