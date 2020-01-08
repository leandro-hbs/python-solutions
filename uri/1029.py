valores = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986]
vetor = {0:1, 1:1}

def fib(n):
    global vetor
    if n in vetor:
        return vetor[n]
    else:
        vetor[n] = fib(n-1) + fib(n-2) + 1
        return vetor[n]

N = int(input())
for i in range(N):
    num = int(input())
    print('fib({}) = {} calls = {}'.format(num, fib(num)-1, valores[num]))