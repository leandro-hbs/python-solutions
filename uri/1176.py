def fib(n):
    vetor = []
    vetor.append(0)
    vetor.append(1)
    for i in range(2,n+1,1):
        vetor.append(vetor[i-1] + vetor[i-2])
    return vetor[n]

n = int (input())
for i in range (n):
  num = int(input())
  print ("Fib({}) = {}".format(num,fib(num)))