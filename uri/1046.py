i, f = list(map(int,input().split()))

if i >= f:
    f = f+24
print('O JOGO DUROU {} HORA(S)'.format(f-i))