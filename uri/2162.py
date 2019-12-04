par = 0
picovale = 0
  
def pico_vale(lista):
  vales = []
  for i in range(len(lista)-1):
    if lista[i] - lista[i+1] == 0:
      return 0
    if lista[i] - lista[i+1] < 0:
      vales.append(0)
    elif lista[i] - lista[i+1] > 0:
      vales.append(1)
  if lista[-1] > lista[-2]:
    vales.append(1)
  else:
    vales.append(0)
  return vales

n = int(input())
alturas = input().split()
alturas =  [int(x) for x in alturas]

f = pico_vale(alturas)

if f != 0:
  for i in range(len(f) - 1):
    if f[i] == f[i+1]:
      picovale = 0
      break
    else:
      picovale = 1

print(picovale)