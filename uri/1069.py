def diamantes(entrada):
    diamante = 0
    contador = 0
    for i in entrada:
        if i == '<':
            contador += 1
        if i == '>':
            if contador > 0:
                contador -= 1
                diamante += 1 
    return diamante

N = int(input())
for i in range(N):
    entrada = input()
    print(diamantes(entrada))