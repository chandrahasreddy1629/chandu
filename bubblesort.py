a = [100,100,8,9,7,5,6]
n = len(a)
swapped = False
for i in range(0,n):

    for j in range(0,n-1):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            swapped = True

print(a)

