vetor = []
while True:
    try:
        num = float(input())
        if num > 0:
            vetor.append(num)
    except:
        break
print(str(len(vetor)) + ' valores positivos')
