class Animal:
    def legs(self):
        print("i have four leg")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def dogname(self):
        print(f"this is a {self.name}")

a = Dog("germanshepard")
print(a.dogname())
print(a.legs())
        