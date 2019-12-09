x, y = map(int, input().split())

if (x < y):
    print('O JOGO DUROU {} HORA(S)'.format(y-x))
else:
    z = 24 - x
    print('O JOGO DUROU {} HORA(S)'.format(z+y))