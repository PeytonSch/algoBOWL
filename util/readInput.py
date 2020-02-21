def readInputFile(inputList,inputFilePath):
    #read in the file
    inputFile = open(inputFilePath, 'r')

    for line in inputFile:
        line = line.strip()
        currentLine = []
        currentLine = line.split()
        inputList.append(currentLine)
    inputFile.close()

    return inputList
