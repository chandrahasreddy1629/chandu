def fibnosiNumber(n):
    a = 0
    b = 1
    c = 0
    for i in range(n):
        a = b
        b = c
        c = a+b
        print(c)
    return n
f = 10
result = fibnosiNumber(f)

