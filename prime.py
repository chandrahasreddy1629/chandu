n = 12
isprime = True

for x in range(2,n):
   if( n % x == 0):
        isprime = False
        break

if (isprime == True):
    print("prime")
else:
    print("composite")
