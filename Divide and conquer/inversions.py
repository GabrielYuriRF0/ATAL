from math import inf

def countSplit(array, left, right, middle):
    n1 = middle - left + 1
    n2 = right - middle
    count = 0
    
    l = [0] * (n1 + 1)
    r = [0] * (n2 + 1)
    
    for i in range(n1):
        l[i] = array[left + i]
    for j in range(n2):
        r[j] = array[middle + 1 + j]
    
    l[n1] = inf
    r[n2] = inf
    
    i = 0
    j = 0
    
    for k in range(left, right + 1):
        if l[i] <= r[j]:
            array[k] = l[i]
            i += 1
        else:
            array[k] = r[j]
            count += (n1 - i)  
            j += 1
    
    return count
    
def countInversions(array, left, right):
    if left >= right:
        return 0
    middle = (left + right) // 2
    x = countInversions(array, left, middle)
    y = countInversions(array, middle + 1, right)
    z = countSplit(array, left, right, middle)
    return x + y + z

array = list(map(int, input().split()))
print(countInversions(array, 0, len(array) - 1))
