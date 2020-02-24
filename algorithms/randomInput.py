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

        n1 = sign1 * n1
        n2 = sign2 * n2

        if(n1 == -7):
            n1 = 7
        if (n2 == 13):
            n2 = -13
        if(n1 == 5):
            n1 = random.randint(1,n_variables)
            n1 = sign1 * n1
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1


        chance = random.randint(1,100)

        if(chance < 30):
            n1 = -1 * n1
            n2 = -1 * n2

        if(n1 == 1 and chance < 85):
            n1 = -1
        if(n1 == 2 and chance < 80):
            n1 = -2
        if(n1 == 3 and chance < 75):
            n1 = -3
        if(n1 == 4 and chance < 70):
            n1 = -4
        if(n1 == 5 and chance < 65):
            n1 = -5
        if(n1 == 6 and chance < 90):
            n1 = -6

        if(n2 == 1 and chance < 65):
            n2 = -1
        if(n2 == 2 and chance < 78):
            n2 = -2
        if(n2 == 3 and chance < 92):
            n2 = -3
        if(n2 == 4 and chance < 83):
            n2 = -4
        if(n2 == 5 and chance < 74):
            n2 = -5
        if(n2 == 6 and chance < 76):
            n2 = -6

        if(n1 == 11 and chance < 65):
            n1 = 11
        if(n1 == 12 and chance < 60):
            n1 = 12
        if(n1 == 13 and chance < 75):
            n1 = 13
        if(n1 == 14 and chance < 70):
            n1 = 14
        if(n1 == 15 and chance < 65):
            n1 = 15
        if(n1 == 16 and chance < 90):
            n1 = 16

        if(n2 == 11 and chance < 65):
            n2 = -11
        if(n2 == 12 and chance < 78):
            n2 = -12
        if(n2 == 13 and chance < 92):
            n2 = -13
        if(n2 == 14 and chance < 83):
            n2 = -14
        if(n2 == 15 and chance < 74):
            n2 = 15
        if(n2 == 16 and chance < 76):
            n2 = 16


        if(n1 == 14 and chance < 43):
            n1 = random.randint(1,n_variables)
            n1 = sign1 * n1
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n2 == 14 and chance < 10):
            n2 = random.randint(1,n_variables)
            n2 = sign2 * n2
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n1 == 1 and chance < 43):
            n1 = random.randint(1,n_variables)
            n1 = sign1 * n1
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n2 == 1 and chance < 34):
            n2 = random.randint(1,n_variables)
            n2 = sign2 * n2
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n1 == 4 and chance < 43):
            n1 = random.randint(1,n_variables)
            n1 = sign1 * n1
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n2 == 4 and chance < 83):
            n2 = random.randint(1,n_variables)
            n2 = sign2 * n2
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n1 == 7 and chance < 19):
            n1 = random.randint(1,n_variables)
            n1 = sign1 * n1
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n2 == 7 and chance < 35):
            n2 = random.randint(1,n_variables)
            n2 = sign2 * n2
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1

        if(n1 == 11 and chance < 43):
            n1 = random.randint(1,n_variables)
            n1 = sign1 * n1
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n2 == 11 and chance < 10):
            n2 = random.randint(1,n_variables)
            n2 = sign2 * n2
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n1 == 17 and chance < 43):
            n1 = random.randint(1,n_variables)
            n1 = sign1 * n1
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n2 == 17 and chance < 34):
            n2 = random.randint(1,n_variables)
            n2 = sign2 * n2
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n1 == 6 and chance < 43):
            n1 = random.randint(1,n_variables)
            n1 = sign1 * n1
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n2 == 6 and chance < 83):
            n2 = random.randint(1,n_variables)
            n2 = sign2 * n2
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n1 == 9 and chance < 19):
            n1 = random.randint(1,n_variables)
            n1 = sign1 * n1
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1
        if(n2 == 9 and chance < 35):
            n2 = random.randint(1,n_variables)
            n2 = sign2 * n2
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
                n1 = sign1 * n1

        if(n1 == 15 and chance < 65):
            n2 = 8
        if(n2 == -18 and chance < 21):
            n1 = -19
        if(n1 == 7 and chance < 85):
            n2 = -4
        if(n2 == 2 and chance < 48):
            n1 = -7
        if(n1 == 2 and chance < 64):
            n2 = 8
        if(n2 == 14 and chance < 351):
            n1 = 20
        if(n1 == 5 and chance < 85):
            n2 = 6
        if(n2 == -3 and chance < 68):
            n1 = -5
        if(n1 == 5 and chance < 55):
            n2 = 13
        if(n2 == 13 and chance < 45):
            n1 = -4
        if(n1 == -12 and chance < 36):
            n2 = 12
        if(n2 == 17 and chance < 74):
            n1 = -4




        if(chance < 7):
            while(n1 == n2):
                n1 = random.randint(1,n_variables)
            while(n1 == -1*n2):
                n1 = random.randint(1,n_variables)

        while(n1 == n2):
            n1 = random.randint(1,n_variables)
        while(n1 == -1*n2):
            n1 = random.randint(1,n_variables)

        toWrite = str(n1) + " "  + str(n2) + "\n"
        outFile.write(toWrite)

    outFile.close()
