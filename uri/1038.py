x = input().split()

a, b = x
a = int(a)
b = int(b)
z = 0
l = {1:4, 2:4.5, 3:5, 4:2, 5:1.5}

for i in l:
    z = l.get(a) * b
print("Total: R$ {0:.2f}".format(z))