def aToB(a, b, currentValue, i, steps):
    steps.append(currentValue)
    if currentValue == b:
        return steps
    
    elif currentValue < b:
        result1 = None
        result2 = None
        result3 = None
        result4 = None
        if i == 0:
            result1 = aToB(a,b, a *2, i+1, steps[:])
            result2 = aToB(a,b, (10 * a) + 1, i+1, steps[:])
        else:
            result3 = aToB(a,b, currentValue *2, i+1, steps[:])
            result4 = aToB(a,b, (10 * currentValue) + 1, i+1, steps[:])
    
        if result1:
            return result1
        elif result2:
            return result2
        elif result3:
            return result3
        elif result4:
            return result4
        else:
            return None        
        
a,b = input().split(' ')
a = int(a)
b = int(b)
steps = []

result = aToB(a,b,a,0, steps)
if result != None:
    print("YES")
    print(len(result))
    elements = ''
    for element in result:
        elements += str(element) + " "
    print(elements)
else:
    print('NO')  