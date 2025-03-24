# Algoritmo da mochila binária

- Dado um conjunto de itens com seus respectivos pesos e valores, achar a melhor combinação deles que maximize o valor e não ultrapasse a capacidade da mochila

## Implementação

```python
def mochila_binaria(valores, pesos, capacidade):
    n = len(valores)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n +1):
        for w in range(0, capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-pesos[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacidade]
```

## Complexidade

- A sua complexidade é O(n \* capacidade)
