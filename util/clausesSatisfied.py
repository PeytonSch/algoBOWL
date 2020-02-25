def clausesSatisfied2(input,clauses):
    trueClauses = 0
    for clause in clauses:
       if int(clause[0]) < 0 and int(input[abs(int(clause[0])) -1]) == 0:
           if int(clause[1]) < 0 and int(input[abs(int(clause[1])) -1]) == 0 or int(clause[1]) > 0 and int(input[abs(int(clause[1])) -1]) == 1:
               trueClauses = trueClauses + 1
       elif  int(clause[0]) > 0 and int(input[abs(int(clause[0])) -1]) == 1:
           if int(clause[1]) < 0 and int(input[abs(int(clause[1])) -1]) == 0 or int(clause[1]) > 0 and int(input[abs(int(clause[1])) -1]) == 1:
               trueClauses = trueClauses + 1
    return trueClauses



def clausesSatisfied(ans, inputLines):
    numberSatisfied = 0


    for clause in inputLines:
        #each clause is [#, #]
        if(int(clause[0]) > 0 and int(clause[1]) > 0):
            #both clauses are as is
            result = ans[abs(int(clause[0]))-1] or ans[abs(int(clause[1]))-1]
        elif(int(clause[0]) < 0 and int(clause[1]) < 0):
            #both clauses are not
            result = not ans[abs(int(clause[0]))-1] or not ans[abs(int(clause[1]))-1]
        elif(int(clause[0]) > 0 and int(clause[1]) < 0):
            #2nd clause is not
            result = ans[abs(int(clause[0]))-1] or not ans[abs(int(clause[1]))-1]
        elif(int(clause[0]) < 0 and int(clause [1]) > 0):
            #first clause is not
            result = not ans[abs(int(clause[0]))-1] or ans[abs(int(clause[1]))-1]

        if result is True:
            numberSatisfied = numberSatisfied + 1

    return numberSatisfied
