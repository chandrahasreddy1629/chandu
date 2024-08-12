def checkPrime(list):
    n = len(list)
    for i in range(0,n):
        isprime = True
        for x in range(2,list[i]):
            if(list[i]%x==0):
                isprime = False
                break
        if isprime:
            list[i] = "prime"
        else:
            list[i] = "composite"
    return list

list = [2,3,4,5,6,7,8,6,4,6]
cp = checkPrime(list)
print(cp)
