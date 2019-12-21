def arvore_binaria(vetor):
    if len(vetor) == 1:
        print(vetor)
        return(vetor)
    meio = int(len(vetor)/2)
    arvore_binaria(vetor[:meio])
    arvore_binaria(vetor[meio+1:])

global vetor
vetor = input().split()
vetor = [int(elem) for elem in vetor]
vetor = sorted(vetor)
arvore_binaria(vetor)