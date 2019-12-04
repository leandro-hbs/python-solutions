while True:
    try:
        numeros = input().split()
        V = int(numeros[0])
        T = int(numeros[1])
        print (V*T*2)
    except:
        break