def imposto(salario):
    if salario <= 3000:
        return (salario-2000)*0.08
    elif salario <= 4500:
        return imposto(3000) + (salario-3000)*0.18
    else:
        return imposto(4500) + (salario-4500)*0.28

salario = float(input())
if salario <= 2000:
    print("Isento")
else:
    print('R$ %.2f' %(imposto(salario))) 