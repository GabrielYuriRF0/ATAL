
from math import inf

def calculateCost(currentSolution):
    cost = 0
    for i in range(0, len(currentSolution)):
        if(currentSolution[i] != None):
            cost += mapAgentsTasks[currentSolution[i]  + str(i +1)]

    return cost
def generatePermutations(currentSolution, agents, i, n, minCost):
    if i == n:
        currentCost = calculateCost(currentSolution[:])
        if currentCost < minCost[0]:
            minCost[0] = currentCost
            if(len(currentSolution) > 0):
                bestSolution.append(currentSolution[:])

    else:
        for j in range(0,n):
            if agents[j] not in currentSolution:
                currentSolution[i] = agents[j]
                currentCost = calculateCost(currentSolution)
                if currentCost > minCost[0]:
                    continue
                generatePermutations(currentSolution[:], agents,i+1, n, minCost)
                    

agents = ['a','b','c','d']
n = len(agents)
mapAgentsTasks = {'a1': 11, 'a2':12, 'a3':18,'a4':40,
                  'b1':14,'b2':15,'b3':13, 'b4':22,
                  'c1':11, 'c2':17, 'c3':19, 'c4':23,
                  'd1':17, 'd2':14, 'd3':20, 'd4':28}
bestSolution = []

generatePermutations([None] * n, agents,0,n, [inf])

print(bestSolution[-1])



