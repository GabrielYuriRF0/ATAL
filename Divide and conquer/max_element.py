from math import inf
def getMaxElement(array, left, right):
    if left >= right:
        if array[left] > result[0]:
            result[0] = array[left]
    else:
        middle = int((left + right) / 2)
        getMaxElement(array, left, middle)
        getMaxElement(array, middle + 1, right)

result = [-inf]
array = list(map(int, input().split()))
getMaxElement(array,0, len(array) - 1)
print(result[0])

'''
f(n) = 1
T(n) = 2T(n/2) + 1
a = 2
b = 2
Pelo primeiro caso do método mestre, o custo do algoritmo é tem o seguinte custo:
T(n) = θ(n ** log a b) = T(n) = θ(n)
'''
