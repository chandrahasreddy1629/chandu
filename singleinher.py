class parent:
    def function(self):
        print("function1")

class child(parent):
    def function2(self):
        print("function2")

obj1 = child()

obj1.function2() #function one eppudu vastundhi ante child lo parent ni pettinappudu
obj1.function()
