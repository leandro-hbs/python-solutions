tupla = {''}

while True:
  try:
    joias = input()
    if joias == '':
      break
    else:
      tupla.add(joias)
  except:
    break
print(len(tupla)-1)