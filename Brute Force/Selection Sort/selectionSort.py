def selectionSort(array):
    arraySize = len(array)

    for i in range(0, arraySize - 1):
        indexSmaller = i
        for j in range(i+1, arraySize):
            if array[j] < array[indexSmaller]:
                indexSmaller = j
        
        aux = array[i]
        array[i] = array[indexSmaller] 
        array[indexSmaller] = aux
    
    return array


array1 = [1,2,3]
array2 = [4,5,3]
array3 = [2,1,4,7,0,2]

print(selectionSort(array1))
print(selectionSort(array2))
print(selectionSort(array3))

