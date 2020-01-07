import bisect

def quicksort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return array

def binary_search(array, item):
    i = bisect.bisect_left(array, item)
    return i if i < len(array) and array[i] == item else -1

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
            marmores = quicksort(marmores)
        if i >= num:
            digit = int(input())
            val = binary_search(marmores, digit)
            if val == -1:
                print(str(digit) + ' not found')
            else:
                print(str(digit) + ' found at ' + str(val+1))
    cont+=1