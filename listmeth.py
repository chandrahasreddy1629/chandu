l1 = [1,2,3,4]
# append add an element at the end of the list
l1.append(100)
print(l1)
#clear
l2 = [10,11,12]
print(l2)
l2.clear()
print(l2)
l2.append(1000)
print(l2)

#copy
l3= ["hasu","ram","anu"]
c= l3.copy()
print(c)
#count
l4 = [10,10,10,10,11,11,11,11,12,12]
cnt = l4.count(10)
print(cnt)

# insert
l5 = [11,12,13,14,15]
l5.insert(1,"hasu")
print(l5)

# pop
l6 = [15,16,17,18]
l6.pop()
print(l6)
l6.pop(1)
print(l6)

#remove
l7=[1,1,1,1,1,1,"ram","ram",2,2,2]
l7.remove("ram")
print(l7)

#length
l7_length = len(l7)
print(l7_length)