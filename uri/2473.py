N = input().split()
S = input().split()	

R=0
for i in N:
    if i in S:
        R+=1

if (R<=2):
    print ("azar")
if (R==3):
    print ("terno")
if (R==4):
    print ("quadra")
if (R==5):
    print ("quina")
if (R==6):
    print ("sena")
