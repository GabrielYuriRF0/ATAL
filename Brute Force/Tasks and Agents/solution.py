
from math import inf

def generatePermutations(currentSolution, agents, i, n):
    if i == n:
        permutations.append(currentSolution[:])
    else:
        for j in range(0,n):
            if agents[j] not in currentSolution:
                currentSolution[i] = agents[j]
                generatePermutations(currentSolution[:], agents,i+1, n)


agents = ['a','b','c','d']
n = len(agents)
mapAgentsTasks = {'a1': 11, 'a2':12, 'a3':18,'a4':40,
                  'b1':14,'b2':15,'b3':13, 'b4':22,
                  'c1':11, 'c2':17, 'c3':19, 'c4':23,
                  'd1':17, 'd2':14, 'd3':20, 'd4':28}

permutations = []
generatePermutations([None] * n, agents,0,n)
minCust = inf
bestSolution = None

for permutation in permutations:
    currentCust = 0
    for i in range(0, len(permutation)):
        currentCust += mapAgentsTasks[permutation[i] + str(i+1)]

    if currentCust < minCust:
        minCust = currentCust
        bestSolution = permutation

print(bestSolution)



