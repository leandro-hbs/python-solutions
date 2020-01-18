def minimum(tamanho, valores, tabela):
    for i in range(tamanho+1):
        cont = i
        for j in [c for c in valores if c <= i]:
            if tabela[i-j] + 1 < cont:
                cont = tabela[i-j]+1
        tabela[i] = cont
    return tabela[i]

T = int(input())
for i in range(T):
    tabela = [0]*1000001
    N, M = list(map(int,input().split()))
    valores = list(map(int,input().split()))
    print(minimum(M,valores,tabela))