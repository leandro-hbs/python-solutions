vetor = [None]*10000

def minimumcoin(tamanho, valores):
    global vetor
    minimo = tamanho
    if tamanho in valores:
        vetor[tamanho] = 1
        return 1
    elif vetor[tamanho] != None:
        return vetor[tamanho]
    else:
        for i in [c for c in valores if c <= tamanho]:
                num = 1 + minimumcoin(tamanho-i,valores)
                if num < minimo:
                    minimo = num
                    vetor[tamanho] = minimo
    return minimo