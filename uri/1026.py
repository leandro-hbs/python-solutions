while True:
    try:
        n1, n2 = list(map(int,input().split()))
        print(int(n1 ^ n2))
    except:
        break