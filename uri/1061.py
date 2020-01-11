dia_inicio = (input().split())
w = int(dia_inicio[0])
hora_inicio = input().split(":")
x = int(hora_inicio[0])
y = int(hora_inicio[1])
z = int(hora_inicio[2])

dia_final = (input().split())
w2 = int(dia_final[0])
hora_final = input().split(":")
x2 = int(hora_final[0])
y2 = int(hora_final[1])
z2 = int(hora_final[2])

dia = w2 - w

hora = x2 - x
if(hora < 0):
	hora = 24 + hora
	dia = dia - 1

minuto = y2 - y
if(minuto < 0):
	minuto = 60 + minuto
	hora = hora - 1


segundo = z2 - z
if(segundo < 0):
	segundo = 60 + segundo
	minuto = minuto - 1

if(dia <= 0):
	dia = 0

print("{} dia(s)".format(dia))
print("{} hora(s)".format(hora))
print("{} minuto(s)".format(minuto))
print("{} segundo(s)".format(segundo))