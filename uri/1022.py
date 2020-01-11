def mdc(n1,n2):
    if n1%n2 == 0:
        return n2
    else:
        return mdc(n2,n1%n2)

N = int(input())

for i in range(N):
    n = input().split()
    operador = n[3]
    if operador == '+':
        numerador = (int(n[0])*int(n[6]))+(int(n[2])*int(n[4]))
        denominador = int(n[6])*int(n[2])
        divisor = mdc(numerador,denominador)
        print(str(numerador) + '/' + str(denominador) + ' = ' + str(int(numerador/divisor)) + '/' + str(int(denominador/divisor)))
    if operador == '-':
        numerador = (int(n[0])*int(n[6]))-(int(n[2])*int(n[4]))
        denominador = int(n[6])*int(n[2])
        divisor = mdc(numerador,denominador)
        print(str(numerador) + '/' + str(denominador) + ' = ' + str(int(numerador/divisor)) + '/' + str(int(denominador/divisor)))
    if operador == '*':
        numerador = int(n[0])*int(n[4])
        denominador = int(n[2])*int(n[6])
        divisor = mdc(numerador,denominador)
        print(str(numerador) + '/' + str(denominador) + ' = ' + str(int(numerador/divisor)) + '/' + str(int(denominador/divisor)))
    if operador == '/':
        numerador = int(n[0])*int(n[6])
        denominador = int(n[4])*int(n[2])
        divisor = mdc(numerador,denominador)
        print(str(numerador) + '/' + str(denominador) + ' = ' + str(int(numerador/divisor)) + '/' + str(int(denominador/divisor)))