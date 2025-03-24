from math import inf
min = [inf]
max = [-inf]

def min_max(array, left, right):
    if left >= right:
        if array[left] < min[0]:
            min[0] = array[left]
        
        if array[left] > max[0]:
            max[0] = array[left]
    else:
        middle = (left + right) // 2
        min_max(array, left, middle)
        min_max(array, middle + 1, right)

array = list(map(int, input().split()))
min_max(array, 0, len(array) - 1)
print(min[0], max[0])