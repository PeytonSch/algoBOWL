#Libraries
import itertools

#Util files
from util.readInput import *
from algorithms.exhaustive import *
from algorithms.localMax import *

#Algorithms


#lines from input file
inputLines = []
n_variables = 0
m_clauses = 0

#read input from input file and store in input lines
readInputFile(inputLines,'./inputs/input1.txt')

#set m_clauses and n_variables from the first line of the input file
m_clauses = inputLines[0][0]
n_variables = inputLines[0][1]

#remove first line that just contains m and n
inputLines.pop(0)

#contains all permutations of TF combinations to test
allTfCombinations = []
tfList = [False,True]
allTfCombinations = list(itertools.product(tfList,repeat=int(n_variables)))

runExhaustiveAlgorithm(inputLines,allTfCombinations,m_clauses,n_variables)
bestSolution = [1] * int(n_variables)
runLocalMax(n_variables,bestSolution,inputLines)
