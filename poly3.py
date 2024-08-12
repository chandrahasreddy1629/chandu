class India():
    def capital(self):
        print("the capital india is delhi")
    def language(self):
        print("the language of india is hindi")

    def cont(self):
        print("india is asian continent")

class Usa():
    def capital(self):
        print("the capital of usa is washington")
    def language(self):
        print("the langue of usa is english")

    def cont(self):
        print("usa is in americian continent")

def func(obj):
    obj.capital()
    obj.language()
    obj.cont()

i1 = India()
a1 = Usa()

func(i1)
func(a1)