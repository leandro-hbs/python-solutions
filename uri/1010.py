p1 = (input()).split(" ")
p2 = (input()).split(" ")

codigo1 = int (p1[0])
n1 = int (p1[1])
valor1 = float (p1[2])

codigo2 = int (p2[0])
n2 = int (p2[1])
valor2 = float (p2[2])

total = (n1 * valor1) + (n2 * valor2)

print ("VALOR A PAGAR: R$ %.2f" %total)