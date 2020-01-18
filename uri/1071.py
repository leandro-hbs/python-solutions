I = int(input())
F = int(input())
cont = 0
if I > F:
    aux = F
    F = I
    I = aux
if I%2 == 0:
    for i in range(I+1,F,2):
        cont += i
else:
    for j in range(I+2,F,2):
        cont += j
print(cont)