def mdc(n1,n2):
    if n1%n2 == 0:
        return n2
    else:
        return mdc(n2,n1%n2)

N = int(input())

for i in range(N):
    n1, n2 = list(map(int,input().split()))
    print(mdc(n1,n2))