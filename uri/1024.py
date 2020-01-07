N = int(input())

def ascii(palavra):
    for i in range(len(palavra)):
        palavra = palavra[:i] + chr(ord(palavra[i]) + -1) + palavra[i+1:]
    return palavra

for i in range(N):
    palavra = input()
    metade = int(len(palavra)/2)
    for i in range(len(palavra)):
        if palavra[i].isalpha():
            palavra = palavra[:i] + chr(ord(palavra[i]) + 3) + palavra[i+1:]
    palavra = palavra[::-1]
    palavra = palavra[:metade] + ascii(palavra[metade:])
    print(palavra)