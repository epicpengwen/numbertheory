

def lin(a , b):
    """
    method for solving ax+by= gcd(a, b)
    x1 + k (b/g) , y1 − (a/g)
    returns(x, y, g)
    since every solution is obtained by (x+(k*b), y - (k *a)) 
    """
    x = 1
    g = a
    v = 0
    w = b
    while (w != 0):
        t = g%w
        q = int(g/w)
        s = x - (q * v)
        x = v
        g = w
        v = s
        w = t
        #print(x,g,v,w)
    if (x < 0):
        #print(x)
        return(x + b, (-1 * (g - (a * x))/b) - a)
    else:
        return(x, (g - (a * x))/b, g)

def linu(a , b):
    """
    method for solving ax+by= gcd(a, b)
    x1 + k (b/g) , y1 − (a/g)
    since every solution is obtained by (x+(k*b), y - (k *a))...
    returns positive x
    """
    x = 1
    g = a
    v = 0
    w = b
    while (w != 0):
        t = g%w
        q = int(g/w)
        s = x - (q * v)
        x = v
        g = w
        v = s
        w = t
        #print(x,g,v,w)
    while (x < 0):
        x += b
    return(x)

def linx(a , b , c):
    q, r = divmod(a,b)
    if r == 0:
        return(0)
    else:
        sol = linx( b, r, c ) 
        u = sol[0]
        v = sol[1]
        return(v)

def solve_Dioph(a,b,c):
    m1=1
    m2=0
    n1=0
    n2=1
    r1=a
    r2=b
    while r1%r2!=0:
        q=r1//r2
        aux=r1%r2
        r1=r2
        r2=aux
        aux3=n1-(n2*q)
        aux2=m1-(m2*q)
        m1=m2
        n1=n2
        m2=aux2
        n2=aux3
    return m2*c #,n2c
