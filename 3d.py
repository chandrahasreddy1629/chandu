list = [
    [
        [1,2,3],
        [1,2,4],
        [4,5,6]
    ],
    [
        [23,45,56],
        [54,34,12],
        [44,55,66]
    ]
]

print (list)
sum = 0

for i in list:
    for j in i:
        for k in j:
            sum += k
print(sum)