#clauses, #variables
#each variable is [1,n] or [-1,-n]
#n needs to be 2<= n <= 1000
#m needs to be 1<= m <= 50000
#want m >> n
#output needs to be n+1 lines



import random

def generateRandomInputFile(m_clauses, n_variables):
    outFile = open("output.txt","w+")
    toWrite = str(m_clauses) + " " + str(n_variables) + "\n"
    outFile.write(toWrite)
    for m in range(1,m_clauses+1):

        #need some logic for choosing positive or negative n
        sign1 = random.choice([-1,1])
        sign2 = random.choice([-1,1])
        #write two n's, must not be the same n
        n1,n2 = 0,0

        while(n1 == n2):
            n1 = random.randint(1,n_variables)
            n2 = random.randint(1,n_variables)
        toWrite = str(n1) + " "  + str(n2) + "\n"
        outFile.write(toWrite)

    outFile.close()
