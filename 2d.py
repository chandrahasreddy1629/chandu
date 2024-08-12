list = [
    [1,2,3,4,5],
    [2,3,4,56,76],
    [4,2,4,5,2,5,7,8],
    [222,332,44,66]
]

print(list)

sum = 0
print(len(list))

for i in list:
    print(len(i))
    for j in i:
        sum += j

print(sum)