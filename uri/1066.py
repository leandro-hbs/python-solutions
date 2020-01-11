pares = []
positivos = []
for i in range(5):
    num = float(input())
    if num%2==0:
        pares.append(num)
    if num > 0:
        positivos.append(num)
    if num == 0:
        var = 4
print(str(len(pares)) + ' valor(es) par(es)')
print(str(abs(len(pares)-5)) + ' valor(es) impar(es)')
print(str(len(positivos)) + ' valor(es) positivo(s)')
print(str(abs(len(positivos)-var)) + ' valor(es) negativo(s)')