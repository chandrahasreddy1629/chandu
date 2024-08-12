file = open("Hello.txt","r")

#print(file.read())
#print(file.read().upper())

#for sent in file:
#    for letter in sent:
#        print(letter)

#print(file.read(5))

for line in file:
    l=line.split()
    sentlen = len(l)
    for x in range(0,sentlen):
        if x%2==0:
            l[x] = l[x].upper()
    print(l)
