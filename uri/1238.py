N = int(input())

for i in range(N):
    result = ''
    palavra = input().split()
    primeira = palavra[0]
    segunda = palavra[1]
    n1 = len(primeira)
    n2 = len(segunda)
    if n1 < n2:
        for j in range(len(primeira)):
            result += primeira[j] + segunda[j]
        result += segunda[n1:]
    elif n1 > n2:
        for j in range(len(segunda)):
            result += primeira[j] + segunda[j]
        result += primeira[n2:]
    else:
        for j in range(len(segunda)):
            result += primeira[j] + segunda[j]
    print (result)