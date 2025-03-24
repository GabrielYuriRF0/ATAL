# Algoritmo de Djkistra

- Esse algoritmo encontra os menores caminhos entre o nó dado e todos os outros de um grafo.

## Implementação:

```python
import heapq

def dijkistra(grafo, origem):
    # Inicializa Distâncias como infinito, exceto para a origem
    distancias = {v:float('inf') for v in grafo}
    distancias[origem] = 0

    fila_prioridade = [(0, origem)] # (distância, origem)

    # Enquanto existir elemento na fila de prioridade
    while fila_prioridade:
        dist_atual, vertice_atual = heapq.heappop(fila_prioridade)  # Extrai o menor

        for vizinho, peso in grafo[vertice_atual].items():
            distancia_nova = dist_atual + peso

            if distancia_nova < distancias[vizinho]:
                distancias[vizinho] = distancia_nova
                heapq.heappush(fila_prioridade, (distancia_nova, vizinho))

    return distancias
```

## Exemplo de uso

```python
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

origem = 'A'
resultado = dijkstra(grafo, origem)

print("Menores distâncias a partir de", origem)
for vertice, distancia in resultado.items():
    print(f"{vertice}: {distancia}")
```

## Complexidade

- A complexidade é O((v \* logv) + e), onde **v** é a quantidade de vértices e **e** a de arestas
