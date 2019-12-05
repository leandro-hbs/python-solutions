class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.adjacentes = []
        self.visitado = False
    
    def add_vizinho(self, vizinho):
        self.adjacentes.append(vizinho)
        self.adjacentes.sort()

class Grafo:
    def __init__(self, tamanho):
        self.vertices = []

    def add_vertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nome not in self.vertices:
            self.vertices.append(vertice)

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
