import math;
n =19
ceal(n/2):
isprime = True
for x in range(2,n/2):
    if(n/2 % x == 0):
        isprime = False
        break
if (isprime == True):
    print("prime")
else:
    print("composite")