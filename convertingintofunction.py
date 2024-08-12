def arraySum(x):
    sum = 0
    for i in x:
        for j in i:
            sum += j
    return sum

a = [
    [1,2,3],
    [2,3,4],
    [3,4,5]
]

asize = arraySum(a)
print(asize)