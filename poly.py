class India():
    def capital(self):
        print("the capital india is delhi")
    def language(self):
        print("the language of india is hindi")

class Usa():
    def capital(self):
        print("the capital of usa is washington")
    def language(self):
        print("the langue of usa is english")
obj1 = India()
obj2 = Usa()

obj1.capital()
obj2.capital()
obj1.language()
obj2.language()

def add(x,y,z=0):
    return x+y+z

r=add(2,3,4)
r1=add(2,3)
print(r)
print(r1)