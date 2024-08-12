file = open("file2.txt","r")
count= 0
for sent in file:
    l = sent.split()
    sentlen=len(l)
    print(l)
    print(sentlen)
    for x in range(0,sentlen):
        if x %2 != 0:
            y = len(l[x])
            print(y)
        
            count = count + y
    print(count)