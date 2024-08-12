l1=[5,2,8,4,1]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
l1.extend([1,2,3])
print(l1)
#string cancadiation
l2=[5,2,1,4,3]
l1=[1,3,5,6,2]
list=l1+l2
print(list)
# string repeatation
s1='hasu'
s=s1*3
print(s)

l3=[1,2,3,4,5]
l3.append(50)
print(l3)
l4=[1,2,3,4,5]
l4.clear()
print(l4)
l5=[1,2,3,4,5,5,5,5]
cnt=l5.count(1)
print(cnt)
l6=[1,2,3,4,5]
l6.insert(2,"ram")
print(l6)

a=range(1,11)
print(a)
print(type(a))

l7=[1,2,3,3,4,4]
l7.remove(4,)
print(l7)
b=len(l7)
print(b)
l7.reverse()
print(l7)
l7.sort()
print(l7)
l7.sort(reverse=True)
print(l7)
t1=(1,2,3,4,5)
a=len(t1)
print(a)
[a1,a2,a3,a4]=["hasu","hari","blue","red"]
print(a1)
print(a2)
print(a3)
print(a4)
from datetime import datetime as dt
print(dt.now())

data = {
    "name" : "hasu",
    "age"  : 22,
    "college" : "aits",
    "branch" : "ece",
    "section" : "a"
}
print(data)
print(data["age"])
data["age"] = 23
print(data)
data["roll_number"] = 429
print(data)
data.pop("branch")
print(data)
print(data.items())
print(data.keys())
print(data.values())
data.update({"sir":"fahim"})
print(data)



n= 85
if (n<=35):
    print("f")
elif(35>n<50):
    print("c")
elif(50>n<80):
    print("b")
else:
    print("a")




