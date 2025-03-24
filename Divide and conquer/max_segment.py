def maxSegment(array, left, right):
    if left == right:
        return array[left]
    q = int((left + right) / 2) 
    x1 = maxSegment(array, left, q)
    x2 = maxSegment(array, q + 1, right)
    y1 = array[q]
    s = array[q]
    for i in range(q-1,left -1, -1):
        s = array[i] + s
        y1 = max(y1,s)

    y2 = array[q + 1]
    s = array[q + 1]

    for j in range(q+2, right):
        s = s + array[j]
        y2 = max(y2,s)
    x = max(x1,y1 + y2, x2)
    return x

array = list(map(int, input().split()))
print(maxSegment(array,0, len(array) - 1))
