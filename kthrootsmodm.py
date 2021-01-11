#first try, the second version is more concise

import math
from eulers_phi import unique, factor_function



##solves x^k = b(mod m) : allows use to input a factorization of m to be used for computing phi(m)
#1.euler phi function
#2.ku - phiv = 1
#3. successive squaring of b^u(mod m)
# function to get unique values 

'''def unique(list1): 

    # intilize a null list 
    unique_list = [] 

    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

listofprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
def factor_function(n):
    factorlist = []
    for i in listofprimes:              #iterating through list of primes to check which factor into n
        while((n/i).is_integer()):
            factorlist.append(i)
            n = n//i
    for i in range(2, int(math.sqrt(n))):   #should i start range from last prime?
        while((n/i).is_integer()):
            factorlist.append(i)
            n = n//i
    if (n != 1):
        factorlist.append(n)
    #print(factorlist)
    answer = 1
    factors = unique(factorlist)
    for i in factors:
        p = i
        k = factorlist.count(p)
        #print(p,k)
        answer = answer * ((p**k) - (p**(k-1)))
        #print(answer)
    return(answer)
'''

def lin(a , b):
    x = 1
    g = a
    v = 0
    w = b1
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

def successivesquaring(a, k, m):
    b = 1
    while k >= 1:
        if k%2 != 0: #if k is odd
            b = (a * b) % m
        a = (a*a) % m
        k = k//2
    return b

def k_roots(k, b, m):
    mphi = 0
    #euler's phi function for m

    if (flist[0] != -1):
        answer = 1
        factors = unique(flist)
        for i in factors:
            p = i
            k = flist.count(p)
            answer = answer * ((p**k) - (p**(k-1)))
        mphi = answer
    else: 
        mphi = factor_function(m)
        #print(mphi)
    #print(mphi)

    #linear equation ku - phiv = 1
    u = lin(k, mphi)
    #print(u)

    #successivesquaring
    return(successivesquaring(b, u, m))


if __name__ == '__main__':
    k = int(input("Enter your value for k: "))
    b = int(input("Enter your value for b: "))
    m = int(input("Enter your value for m: "))


    factorization = (input("Enter a list of a factorization of m separated by spaces (if none enter -1): "))
    #splits input into a string
    strlist = factorization.split() 
    flist = []
    for num in strlist:
        flist.append(int(num))

    print(k_roots(k,b,m))