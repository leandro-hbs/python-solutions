valores = input().split()	
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])
	
maior = (A + B + abs(A - B))/2
maior = int((maior + C + abs(maior - C))/2)
	
print (str(maior) + " eh o maior")