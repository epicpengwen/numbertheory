#a program that solves the congruence ax = c(mod m)
#{if gcd(a,m) does not divide c, return an error message and the value of gcd(a,m)}

#its not really working but i feel like i've implemented it correctly, the linear equations aren't working out the same?
def gcd(a,b):
    r = a % b
    while r > 0:
        a, b, r = b, r, b%r
    return b

def isolve(a, b, c) :
    q, r = divmod(a, b)
    if r == 0:
        return( [0,c/b])
    else :
        sol = isolve(b, r, c)
        u = sol[0]
        v = sol[1]
        return([v, u-q*v])

def solvecongruence(a, c, m):
    listx = isolve(a, -m, gcd(a,m))  #linear congruence theorem
    u = listx[0] 
    v = listx[1]
    g = gcd(a,m)
    print(u, v, g)
    #list that has u,v for solutions to au - mv = g
    #if g does not divide c then no solutions
    if(c % g != 0):
        return("no solutions", g)
    #make a list for all the incongruent solutions
    answers = []
    print(c,v,u)
    x = (c * u / g)     
    for i in range(0, g-1):
        x = x + (i * (m / g)) % m
        answers.append(x)
    return answers

print(solvecongruence(893, 266, 2432))