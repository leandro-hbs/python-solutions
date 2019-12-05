x = input().split()

a, b, c, d = x
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if c > 0 and d > 0 and a%2 == 0 and b > c and d > a and (c+d) > (a+b):
    print('Valores aceitos')
    
else:
    print('Valores nao aceitos')