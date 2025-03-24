# Algoritmo do Segmento de Soma Máxima

- O problema do segmento de soma máxima consistem em encontar o maior valor possível entre todos os segmentos de um array.
- Por exemplo: o array A = [20, -30, 15, -10, 30, -20, -30, 30], tem como o segmento de soma máxima as posições A[2] até A[5], onde a soma é 35.

## Implementação

```python
def segemento_soma_maxima(array):
    n = len(array)
    s = [0] * n
    s[0] = array[0]

    for i in range(1, n):
        s[i] = array[i]
        if s[i -1] >= 0:
            s[i] = s[i] + s[i-1]

    return max(s)
```

## Complexidade:

- O(N)
