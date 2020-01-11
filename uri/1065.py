vetor = []
for i in range(5):
    num = float(input())
    if num%2==0:
        vetor.append(num)
print(str(len(vetor)) + ' valores pares')