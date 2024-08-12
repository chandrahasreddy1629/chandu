def checkPrime(list):
    n = len(list)
    print(n)
    for i in range(0,n):
        isprime = True
        for x in range(2,list[i]):
            if(list[i] % x == 0):
                isprime = False
                break
        if isprime:
            list[i] = "prime"
        else:
            list[i] = "composite"
    return list
list = [4,5,6,7,8,9]
cp = checkPrime(list)
print(cp)
