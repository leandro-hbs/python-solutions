entrada = input().split()

P1 = int(entrada[0])
C1 = int(entrada[1])
P2 = int(entrada[2])
C2 = int(entrada[3])

if P1*C1 == P2*C2:
    print(0)
elif P1*C1 < P2*C2:
    print(1)
else:
    print(-1)