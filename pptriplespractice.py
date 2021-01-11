def primtriples(x, v):
    a = x**2 - v**2
    b = 2 * x * v
    c = x**2 + v**2
    print(a , b , c, "\n")
value = int(input("Give a range: "))
for i in range(1, value, 1):
    v = i
    for j in range(i+1, value, 1):
        u = j
        print(u,v)
        primtriples(u,v)
    