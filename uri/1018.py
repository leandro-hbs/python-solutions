D = int (input())
print (D)

notas = [100, 50, 20, 10, 5, 2, 1]
for i in notas:
    print ("{} nota(s) de R$ {},00".format(int(D/i), i))
    D = D%i