alfa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

N = int(input())

for i in range (N):
    result = ''
    palavra = input()
    num = int(input())
    for let in palavra:
        index = alfa.index(let) + 26 - num
        result += alfa[index]
    print (result)