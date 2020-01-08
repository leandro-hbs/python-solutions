t = int(input())

h = int(t/3600)
m = int((t-h*3600)/60)
s = int(t-(h*3600 + m*60))

print("{}:{}:{}".format(h,m,s))