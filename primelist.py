list = [8,4,2,3,5,6,7,17,11,78]
lst2=[]
for i in list:
    isprime = True
    for x in range(2,i):
        if(i % x == 0):
            isprime = False
            break
    if(isprime == True):
        print("prime")
        lst2.append("prime")

    else:

        print("composite")
        lst2.append("composite")
print(lst2)
