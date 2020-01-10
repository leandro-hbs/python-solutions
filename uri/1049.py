dic1 = {'ave':'0', 'mamifero':'1', 'inseto':'2', 'anelideo':'3', 'carnivoro':'4', 'onivoro':'5', 'herbivoro':'6', 'hematofago':'7'}
dic2 = {'04':'aguia', '05':'pomba', '15':'homem', '16':'vaca', '27':'pulga', '26':'lagarta', '37':'sanguessuga', '35':'minhoca'}

a = input()
b = input()
c = input()
b = dic1[b]
c = dic1[c]
result = b + c

print(dic2[result])