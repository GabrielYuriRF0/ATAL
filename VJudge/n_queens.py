# N-rainhas

def eh_valido(t, i):
    for j in range(i):
        if (t[i] == t[j]) or (abs(t[i] - t[j]) == abs(i - j)):
            return False
    return True

def imprime_rainhas(t, n):
    global resultados
    resultado = ""

    for i in range(n):
        linha = ["."] * n
        linha[t[i]] = "Q"
        nova_linha = "".join(linha)
        resultado += nova_linha
        if i < n - 1:
            resultado += "\n"
    
    resultados.append(resultado)

def n_rainhas(t, i, n):
    if i == n:
        imprime_rainhas(t, n)
    else:
        for j in range(n):
            t[i] = j
            if eh_valido(t, i):
                n_rainhas(t, (i + 1), n)

n = int(input())
tabuleiro = ["."] * n
resultados = []

n_rainhas(tabuleiro, 0, n)

for i in range(len(resultados)):
    if i == len(resultados) - 1:
        print(resultados[i])
    else:
        print(f"{resultados[i]}\n")
