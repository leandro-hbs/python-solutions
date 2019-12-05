x = input().split()

a, b, c = x
a = float(a)
b = float(b)
c = float(c)

if b - c < a and a < b + c and a - c < b and b < a + c and a - b < c and c < a + b:
        print("Perimetro = {0:.1f}".format(a+b+c))
else:
    print("Area = {0:.1f}".format(a+b*c/2))