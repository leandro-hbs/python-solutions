class Grafo:
    def __init__(self, tamanho):
        self.vertices = []
        self.posicoes = {}
        self.matriz = []
        # populando a matriz com 0's
        for i in range(tamanho):
            linha = []
            for j in range(tamanho):
                linha.append(0)
            self.matriz.append(linha)

    def add_vertice(self, nome):
        if nome not in self.vertices:
            self.vertices.append(nome)
            indice = self.vertices.index(nome)
            self.posicoes[nome] = indice
        else:
            return

    def add_aresta(self, inicio, fim, peso = 1):
        if inicio in self.vertices and fim in self.vertices:
            self.matriz[self.posicoes[inicio]][self.posicoes[fim]] = peso
            # se for bidirecional
            self.matriz[self.posicoes[fim]][self.posicoes[inicio]] = peso
        else:
            return

    def mostra_grafo(self):
        for i in range(tamanho):
            for j in range(tamanho):
                print("Linha {} Coluna {} = {}".format(i,j,self.matriz[i][j]))

while True:
    entrada = input().split()
    tamanho = int(entrada[0])
    arestas = int(entrada[1])
    if tamanho == 0 and arestas == 0:
        break
    else:
        grafo = Grafo(tamanho)
        for i in range(arestas):
            valores = input().split()
            inicio = valores[0]
            fim = valores[1]
            peso = valores[2]
            grafo.add_vertice(inicio)
            grafo.add_vertice(fim)
            grafo.add_aresta(inicio, fim, peso)
        grafo.mostra_grafo()
