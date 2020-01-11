def valida(expressao):
    contador = 0
    for i in expressao:
        if i == '(':
            contador += 1
        if i == ')':
            if contador > 0:
                contador -= 1
            else:
                return False
    if contador == 0:
        return True

while True:
    try:
        expressao = input()
        if valida(expressao):
            print('correct')
        else:
            print('incorrect')
    except:
        break