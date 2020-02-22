def clausesSatisfied(input,clauses):
    trueClauses = 0
    for clause in clauses:
       if int(clause[0]) < 0 and int(input[abs(int(clause[0])) -1]) == 0:
           if int(clause[1]) < 0 and int(input[abs(int(clause[1])) -1]) == 0 or int(clause[1]) > 0 and int(input[abs(int(clause[1])) -1]) == 1:
               trueClauses = trueClauses + 1
       elif  int(clause[0]) > 0 and int(input[abs(int(clause[0])) -1]) == 1:
           if int(clause[1]) < 0 and int(input[abs(int(clause[1])) -1]) == 0 or int(clause[1]) > 0 and int(input[abs(int(clause[1])) -1]) == 1:
               trueClauses = trueClauses + 1
    return trueClauses
