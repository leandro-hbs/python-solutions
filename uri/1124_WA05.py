while True:
    L, C, R1, R2 = list(map(int,input().split()))
    if L == 0 and C == 0 and R1 == 0 and R2 == 0:
        break
    tamanho = ((R1-(L-R2))**2 + (R1-(C-R2))**2)**0.5
    diagonal = (L**2 + C**2)**0.5
    if tamanho >= R1 + R2 and diagonal >= R1 * 2 + R2 * 2 and max(R1,R2) < L and max(R1,R2) < C:
        print('S')
    else:
        print('N')