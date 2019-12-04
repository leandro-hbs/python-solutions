pi = 3.14159

valores = input().split()	
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

print ("TRIANGULO: %.3f" %((A*C)/2))
print ("CIRCULO: %.3f" %(pi*C*C))
print ("TRAPEZIO: %.3f" %(((A+B)*C)/2))
print ("QUADRADO: %.3f" %(B*B))
print ("RETANGULO: %.3f" %(A*B))