import math
from eulers_phi import unique, phi_function
from leq import linu
from succsqu import successivesquaring

def kroots(k , b , m):
    """
    solves x^k = b(mod m) : asks for use to unput k, b, m
    allows user to input a factorization of m to be used for computing phi(m)
    
    Steps:
    1.euler phi function
    2.linear equation theorem: ku - phiv = 1
    3.successive squaring of b^u(mod m)
    returns x   
    """
    mphi = 0 #euler's phi function for m

    if flist != []: #if factors not given
        answer = 1
        factors = unique(flist)
        for i in factors:
            p = i
            k = flist.count(p)
            answer = answer * ((p**k) - (p**(k-1)))
        mphi = answer
    else: 
        mphi = phi_function(m)

    #linear equation ku - phiv = 1
    u = linu(k, mphi)

    #successivesquaring
    return(successivesquaring(b, u, m))

if __name__ == '__main__':
    k = int(input("Enter your value for k: "))
    b = int(input("Enter your value for b: "))
    m = int(input("Enter your value for m: "))

    factorization = (input("Enter a list of a factorization of m separated by spaces: "))
    #splits input into a string
    strlist = factorization.split() 
    flist = []
    for num in strlist:
        flist.append(int(num))

    print(kroots(k, b, m))






