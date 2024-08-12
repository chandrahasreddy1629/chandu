def checkPrime(a):
    isprime = True
    for x in range(2,a):
        if a % x == 0:
            isprime = False
            break
    
    return isprime
c = checkPrime(19)
print(c)

