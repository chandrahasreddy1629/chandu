#x = 100
#print(x)
#def fun(i):
#   i+=1
#   print(i)
#fun(x)
#print(x)
#x=100
#print(x)
#for x in range(0,10):
#   print(x)
#print(x)
#y = 10
#for i in range(0,11):
#   z=100
#   print(y)

def scope():
    z = 199
    def inner():
        z = 100
        print(z)

    inner()
    print(z)
scope()
