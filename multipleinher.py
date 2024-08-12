class Father:
    fathername =""
    def father(self):
        print(self.fathername)

class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
class Child(Father, Mother):
    def parents(self):
        print("father" ,self.fathername)
        print("mother" ,self.mothername)
child1 = Child()

child1.fathername = "ram"
child1.mothername = "sita"
child1.parents()
child1.father()
child1.mother()

        