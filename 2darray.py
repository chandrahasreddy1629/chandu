def arraySum(x):
    sum = 0
    for i in x:
        for j in i:
            sum += j
    return sum
a = [
    [1,2,3,4],
    [1,3,4,5],
    [3,5,6,8],
    [5,2,3,4]
]

asize = arraySum(a)
print(asize)
