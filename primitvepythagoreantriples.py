#take users input of a range that will serve! fix code !
value = int(input("Give a range: "))
def primitivetriples(rge):
    for i in range(1, rge, 2):
        t = i
        for j in range(t+2, rge, 2):
            s = j
            a = s * t
            b = (s**2 - t**2) / 2
            c = (s**2 + t**2) / 2
            print(a, b, c)
primitivetriples(value)
