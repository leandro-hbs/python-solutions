def dfs(inicio, grafo):
    global cont
    visitados[inicio] = 1
    for i in grafo[inicio]:
        if visitados[i] == -1:
            cont+=1
            dfs(i,grafo)

T = int(input())
for caso in range(T):
    cont = 0
    N = int(input())
    tamanho = input().split()
    V = int(tamanho[0])
    A = int(tamanho[1])
    grafo = [[] for i in range(V)]
    visitados = [-1 for i in range(V)]
    for i in range(A):
        arestas = input().split()
        I = int(arestas[0])
        F = int(arestas[1])
        grafo[I].append(F)
        grafo[F].append(I)
    dfs(N,grafo)
    print(cont*2)