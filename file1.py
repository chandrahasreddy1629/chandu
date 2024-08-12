file = open("file2.txt","r")
count= 0
for sent in file:
    l = sent.split()
    sentlen=len(l)
    print(l)
    print(sentlen)
    for x in range(0,sentlen):
        if l[x] == "is":
            count = count + 1

print(count)