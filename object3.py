class person:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def __str__(self):
        return f"full name"
    
    def ageCorr(self):
        #x = self.age +12
        return self.age + 11
    
data1 = person("hasu","reddy",44)
print(data1.fname)
print(data1.ageCorr())
        
        
    
