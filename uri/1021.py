N = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]
print('NOTAS:')
for i in notas:
    print ("{} nota(s) de R$ {}.00".format(int(N/i), i))
    N = N%i
N = N * 100
print('MOEDAS:')
for j in moedas:
    print ('%d moeda(s) de R$ %.2f' %(int(N/j), float(j/100))) 
    N = N%j