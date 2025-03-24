# Problema da Subsequência Crescente Máxima

- Consiste em achar a maior subsquência em um array A, exemplo: A = (9, 5, 6, 5, 9, 6, 4, 7), a subsequência máxima seria S = (5, 6, 6, 7)

## Implementação

```python
def subsequencia_crescente_maxima(array):
    n = len(array)
    c = [1] * n

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
                if array[j] <= array[i] and c[j] + 1 > c[i]:
                c[i] = c[j] + 1

    return max(c)
```

## Complexidade

- No pior caso é O(N \*\* 2)
