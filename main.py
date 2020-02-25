#Libraries
import itertools
import time


#Util files
from util.readInput import *
from algorithms.exhaustive import *
from algorithms.localMax import *
from algorithms.randomInput import *

#Algorithms
from algorithms.alg_one import *
from algorithms.alg3 import *
from algorithms.alg2 import *
from algorithms.alg4 import *


#generate input files
#generateRandomInputFile(25000,20)

inputFiles1 = ['./inputs/input_group161.txt']
outputFiles1 = ['./outputs/output_group161.txt']


inputFiles = ['./inputs/input_group136.txt','./inputs/input_group137.txt','./inputs/input_group138.txt','./inputs/input_group139.txt',
            './inputs/input_group140.txt','./inputs/input_group141.txt','./inputs/input_group142.txt','./inputs/input_group143.txt',
            './inputs/input_group144.txt','./inputs/input_group145.txt','./inputs/input_group146.txt','./inputs/input_group147.txt','./inputs/input_group148.txt',
            './inputs/input_group149.txt','./inputs/input_group150.txt','./inputs/input_group151.txt','./inputs/input_group152.txt',
            './inputs/input_group153.txt','./inputs/input_group154.txt','./inputs/input_group155.txt','./inputs/input_group156.txt',
            './inputs/input_group157.txt','./inputs/input_group158.txt','./inputs/input_group159.txt','./inputs/input_group160.txt',
            './inputs/input_group161.txt','./inputs/input_group182.txt']

outputFiles = ['./outputs/output_group136.txt','./outputs/output_group137.txt','./outputs/output_group138.txt','./outputs/output_group139.txt',
            './outputs/output_group140.txt','./outputs/output_group141.txt','./outputs/output_group142.txt','./outputs/output_group143.txt',
            './outputs/output_group144.txt','./outputs/output_group145.txt','./outputs/output_group146.txt','./outputs/output_group147.txt','./outputs/output_group148.txt',
            './outputs/output_group149.txt','./outputs/output_group150.txt','./outputs/output_group151.txt','./outputs/output_group152.txt',
            './outputs/output_group153.txt','./outputs/output_group154.txt','./outputs/output_group155.txt','./outputs/output_group156.txt',
            './outputs/output_group157.txt','./outputs/output_group158.txt','./outputs/output_group159.txt','./outputs/output_group160.txt',
            './outputs/output_group161.txt','./outputs/output_group182.txt']




for f in range(len(inputFiles)):
    #lines from input file
    inputLines = []
    n_variables = 0
    m_clauses = 0
    #read input from input file and store in input lines
    #readInputFile(inputLines,'./inputs/input1.txt')
    readInputFile(inputLines,inputFiles[f])

    #set m_clauses and n_variables from the first line of the input file
    m_clauses = inputLines[0][0]
    n_variables = inputLines[0][1]



    #remove first line that just contains m and n
    inputLines.pop(0)

    #contains all permutations of TF combinations to test
    #allTfCombinations = []
    #tfList = [False,True]
    #allTfCombinations = list(itertools.product(tfList,repeat=int(n_variables)))

    #start = time.time()
    #runExhaustiveAlgorithm(inputLines,allTfCombinations,m_clauses,n_variables)
    #print(time.time()-start)



    firstSolution = [1] * int(n_variables)
    #runLocalMax(n_variables,bestSolution,inputLines)

    algorithm_one(inputLines,m_clauses,n_variables,firstSolution,outputFiles,f)
    #rankInputsAlg2(inputLines,m_clauses,n_variables)
