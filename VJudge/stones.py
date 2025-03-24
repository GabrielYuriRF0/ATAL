def removeStones(stonesHeaps):
    currenSum = 0

    while stonesHeaps[1] >= 1 and stonesHeaps[2] >= 2:
        stonesHeaps[1] -= 1
        stonesHeaps[2] -= 2
        currenSum += 3
    
    while stonesHeaps[0] >= 1 and stonesHeaps[1] >= 2:
        stonesHeaps[0] -= 1
        stonesHeaps[1] -= 2
        currenSum += 3
        
    return currenSum

t = int(input())
for i in range(0,t):
    stonesHeaps = list(map(int, input().split()))
    print(removeStones(stonesHeaps))