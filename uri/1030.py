nc = int(input())

for i in range(nc):
    q, p = list(map(int,input().split()))
    mortos = [i+1 for i in range(q)]
    pivor = 0
    while True:
        if len(mortos) == 1:
            break
        pulos = p + pivor
        while pulos > len(mortos):
            pulos = pulos - len(mortos)
        pivor = pulos -1
        mortos.pop(pivor)
    print('Case {}: {}'.format(i+1, mortos[0]))