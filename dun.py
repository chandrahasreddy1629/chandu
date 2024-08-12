a = [1,2,3,4,5]

def listSize(x):
    sum = 0
    l = len(x)
    for i in x:
        sum += i
    return sum,l
asize = listSize(a)
print(asize)

b = [111,222,333,4444,55,2222]
bsize = listSize(b)
print(bsize)