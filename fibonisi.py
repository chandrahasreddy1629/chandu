n = int(input ("enter the number"))
a = 0
b = 1
c = 0
for i in range (n):
    a=b
    b=c
    c=a+b
    print(c)