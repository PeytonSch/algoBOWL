
def generateOutputToConsole(numClauses,values):
    print(numClauses)
    for v in values:
        if v is True:
            print(1)
        else:
            print(0)


def generateOutputToFile(numClauses,values):
    outfile = open('outputs/output.txt','w+')
    outfile.write(str(numClauses))
    outfile.write("\n")
    for v in values:
        if v is 1:
            outfile.write("1\n")
        else:
            outfile.write("0\n")
    outfile.close()
