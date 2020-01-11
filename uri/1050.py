ddd = {11:'Sao Paulo', 19:'Campinas', 21:'Rio de Janeiro', 27:'Vitoria', 31:'Belo Horizonte', 32:'Juiz de Fora', 61:'Brasilia', 71:'Salvador'}

num = int(input())
if num in ddd:
    print(ddd[num])
else:
    print('DDD nao cadastrado')