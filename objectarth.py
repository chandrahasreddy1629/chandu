class arth:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"arthmetic operation"
    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b
    def substraction(self):
        return self.a - self.b
    
data = arth(100,50)
print(data.addition())
print(data.substraction())
print(data.multiplication())
print(data.division())
        


        