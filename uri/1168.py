dict = {"1":2,"2":5,"3":5,"4":4,"5":5,"6":6,"7":3,"8":7,"9":6,"0":6}
n = int(input())
result = 0

for i in range(n):
    num = input()
    for j in num:
        result += dict[j]
    print("{} leds".format(result))
    result = 0