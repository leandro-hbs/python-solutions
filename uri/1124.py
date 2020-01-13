while True:
    L, C, R1, R2 = list(map(int,input().split()))
    if L + C + R1 + R2 == 0:
        break
    tamanho = ((R1-(L-R2))**2 + (R1-(C-R2))**2)**0.5
    if tamanho >= R1+R2 and L >= R1*2 and L >= R2*2 and C >= R1*2 and C >= R2*2:
        print('S')
    else:
        print('N')