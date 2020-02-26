from util.clausesSatisfied import *

def validate(validateFilePath,inputFilePath):
    inputFile = open(inputFilePath, 'r')
    validateFile = open(validateFilePath, 'r')
    validateList = []
    validateListBool = []
    for line in validateFile:
        line = line.strip()
        currentLine = line.split()
        validateList.append(currentLine)
    validateFile.close()




    inputList = []
    for line in inputFile:
        line = line.strip()
        currentLine = []
        currentLine = line.split()
        inputList.append(currentLine)
    inputFile.close()



    inputList.pop(0)
    numSatisfied = validateList[0]
    validateList.pop(0)

    for i in range(len(validateList)):
        validateListBool.append(int(validateList[i][0]))



    theirSat = numSatisfied[0]
    ourSat = clausesSatisfied(validateListBool,inputList)
    if not (int(theirSat) == int(ourSat)):
        print(validateFilePath)
        print(theirSat)
        print("clauses satisfied " , ourSat)
