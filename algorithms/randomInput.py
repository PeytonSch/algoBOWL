#clauses, #variables
#each variable is [1,n] or [-1,-n]

import random

def generateRandomInputFile(m_clauses, n_variables):
  outFile = open("output.txt","w+")
  f.write(m_clauses, " ", n_variables, "\n")
  for m in range(1,m_clauses):
    for n in range(1,n_variables):
      #need some logic for choosing positive or negative n
      sign1 = random.choice([-1,1])
      sign2 = random.choice([-1,1])
      #write two n's, must not be the same n 
      n1,n2 =0
      while(n1 not equal n2):
        n1 = random.randint(1,n_variables)
        n2 = random.randint(1,n_variables)
      outFile.write(n1, " ", n2, "\n")
  
  outFile.close()
