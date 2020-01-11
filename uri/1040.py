n1, n2, n3, n4 = list(map(float,input().split()))

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4)/10

print('Media: %.1f' %media)
if media < 5:
    print('Aluno reprovado.')
elif media < 7:
    print('Aluno em exame.')
    n5 = float(input())
    print('Nota do exame: %.1f' %n5)
    media = (media + n5)/2
    if media < 5:
        print('Aluno reprovado.')
    else:
        print('Aluno aprovado.')
        print('Media final: %.1f' %media)
else:
    print('Aluno aprovado.')