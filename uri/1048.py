salario = float(input())

if salario <= 400.00:
    percentual = 15
    ganho = (salario * percentual)/100
elif salario <= 800.00:
    percentual = 12
    ganho = (salario * percentual)/100
elif salario <= 1200.00:
    percentual = 10
    ganho = (salario * percentual)/100
elif salario <= 2000.00:
    percentual = 7
    ganho = (salario * percentual)/100
else:
    percentual = 4
    ganho = (salario * percentual)/100

print('Novo salario: %.2f' %(salario + ganho))
print('Reajuste ganho: %.2f' %(ganho))
print('Em percentual: {} %'.format(percentual))