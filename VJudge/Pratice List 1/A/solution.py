from math import ceil

def getListRisk(peopleList):
    listRisk = []
    for element in peopleList:
        if(element <= 9 or element >= 80):
            listRisk.append(True)
        else:
            listRisk.append(False)
    return listRisk

def calculateDays(n,d, peopleList):
    listRisk = getListRisk(peopleList)
    riskNumber = listRisk.count(True)
    noRiskNumber = listRisk.count(False)
    totalDays = ceil(riskNumber/d) + ceil(noRiskNumber/d)
    print(totalDays)

t = int(input())
inputsND = []
listpeopleLists = []
for i in range(0, t):
    n,d = map(int, input().split())
    inputsND.append((n,d))
    peopleList = list(map(int, input().split()))
    listpeopleLists.append(peopleList)

for i in range(0, t):
    n,d = inputsND[i]
    peopleList = listpeopleLists[i]
    calculateDays(n, d, peopleList)


