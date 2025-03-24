n = int(input())
problems = list(map(int, input().split()))
contestsMap = {}

for i in range(0, len(problems)):
    if(problems[i] not in contestsMap.keys()):
        contestsMap[problems[i]] = i

problems = sorted(list(contestsMap.keys()))
days = 0
i = 0

while len(problems) > 0 and  max(problems) >= days:
    problems.remove(problems[0])
    days += 1

print(days)
