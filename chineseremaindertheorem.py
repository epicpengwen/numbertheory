#write a program that takes as input four integers (b,m,c,n) with gcd(m,n) = 1 
# and computes an integer x with 1<=x<m*n satisfying
# x = b(mod m), and x = c (mod n)
def isolve(a, b, c) :
    q, r = divmod(a, b)
    if r == 0:
        return( [0,c/b])
    else :
        sol = isolve(b, r, c)
        u = sol[0]
        v = sol[1]
        return([v, u-q*v])

def chineseremainder(b, m, c, n):
    ylist = isolve(m, n, c - b)
    print(ylist)
    y = ylist[0]  # y is sometimes the negative modulo which is why i added the part below
    y = y%n
    print(m * y + b) 

chineseremainder(3, 37, 1, 87)