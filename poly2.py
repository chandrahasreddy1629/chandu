class Bank():
    def intro(self):
        print("this is a bank in india")

    def nature(self):
        print("this bank is under control of gov of india")

class Sbi(Bank):
    def nature(self):
        print("this is a national bank")

class Apgvb(Bank):
    def nature(self):
        print("this is a state bank")

b1 = Bank()
s1 = Sbi()
a1 = Apgvb()

b1.nature()
b1.intro()
s1.nature()
s1.intro()
a1.nature()
a1.intro()