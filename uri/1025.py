from bisect import bisect_left

def binary_search(array, item):
    i = (bisect_left(array, item))
    return i+1 if i < len(array) and array[i] == item else -1

cont = 1
while True:
    num, con = list(map(int,input().split()))
    if num == 0 and con == 0:
        break
    marmores = []
    print('CASE# {}:'.format(str(cont)))
    for i in range(num+con):
        if i < num:
            marmores.append(int(input()))
        if i == num:
            marmores.sort()
        if i >= num:
            digit = int(input())
            val = binary_search(marmores, digit)
            if val == -1:
                print(str(digit) + ' not found')
            else:
                print(str(digit) + ' found at ' + str(val))
    cont+=1