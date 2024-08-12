class GrandFather:
    def __init__(self, granf):
        self.granf = granf
        self.age = 80
        self.city = "hyd"
    def gfinfo(self):
        print(self.granf, "has the age of",self.age,"city",self.city)

class Father(GrandFather):
    def __init__(self, granf, father):
        self.father = father
        self.fthage = 50
        self.job ="software"
        #super().__init__(granf)
        GrandFather.__init__(self,granf)
    def fatherinfo(self):
        print(self.father,"has the age of", self.fthage, "job", self.job)

class Son(Father, GrandFather):
    def __init__(self, granf,father,son):
        self.son= son
        self.sonage= 20
        self.edu= "btech"
        Father.__init__(self, granf, father)
        #super().__init__(granf,father)

    def soninfo(self):
        print(self.son,"has the age of", self.sonage, "edu",self.edu)



#f1 = Father("raju" , "hari")
#f1.gf()

#print(f1.father)
#print(f1.granf)

s1 = Son("dasaradha", "rama", "lava")

s1.gfinfo()
s1.fatherinfo()
s1.soninfo()


        