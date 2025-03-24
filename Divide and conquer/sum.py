
def calculateSum(array, left, right): 
    if left >= right:
        sum[0] += array[left]
        return
    
    else:
        middle = int((left + right) / 2)
        calculateSum(array,left, middle)
        calculateSum(array, middle + 1, right)
    


array = list(map(int, input().split()))
sum = [0]
calculateSum(array, 0, len(array) -1)
print(sum[0])

'''
O custo desse algoritmo é O(n), pois, apesar de se dividir o array ao meio a cada chamada recursiva,
a operação de soma é executada uma vez para cada elemento do array, deixando o custo O(n).  
'''
