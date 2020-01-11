i, mi, f, mf = list(map(int,input().split()))

if i > f:
    f = f + 24
if i != f and mi > mf:
    f = f - 1
    mf = mf + 60
if i == f and mi > mf:
    f = f + 23
    mf = mf + 60
if i == f and mi == mf:
    f = f + 24

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(f-i, mf-mi))