N = int(input())

IN = 0
OUT = 0
for i in range(N):
    num = int(input())
    if num > 9 and num < 21:
        IN += 1
    else:
        OUT += 1
print(IN,"in")
print(OUT,"out")