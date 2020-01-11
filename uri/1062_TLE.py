def verifica(vetor):
    estacao = [0]
    saida = []
    while len(vetor) > 0:
        maior = max(vetor)
        num = vetor.pop()
        if num == maior and num > estacao[-1]:
            saida.append(num)
        else:
            while num < estacao[-1]:
                saida.append(estacao.pop())
            estacao.append(num)
    while len(estacao) > 1:
        num = estacao.pop()
        saida.append(num)
    if saida == sorted(saida,reverse=True):
        return 'Yes'
    else:
        return 'No'


while True:
    N = int(input())
    if N == 0:
        break
    while True:
        vetor = input().split()
        if vetor[0] == '0':
            print('')
            break
        vetor = [int(i) for i in vetor]
        print(verifica(vetor))