vetor = []
for i in range(6):
    num = float(input())
    if num > 0:
        vetor.append(num)
print(str(len(vetor)) + ' valores positivos')
media = 0
for i in vetor:
    media += i
media = round(media / len(vetor),1)
print(media)