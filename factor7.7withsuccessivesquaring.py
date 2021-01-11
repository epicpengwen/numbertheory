import math, random
listofprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

def factor_function(n):
    factorlist = []
    for i in listofprimes:              #iterating through list of primes to check which factor into n
        while((n/i).is_integer()):
            factorlist.append(i)
            n = n//i
    for i in range(101, int(math.sqrt(n))):   #should i start range from last prime?
        if fermats(n) == True: #if probably prime
            while((n/i).is_integer()):
                factorlist.append(i)
                n = n//i
    if (n != 1):
        factorlist.append(n)
    print(factorlist)


#for i in range(1000000, 1000030):
factor_function(7081)


def successivesquaring(a, k, m):
    b = 1
    while k >= 1:
        if k%2 != 0: #if k is odd
            b = (a * b) % m
        a = (a*a) % m
        k = int(k/2)
    return b


#Write a  program  to  check  if  a  number n is  composite  or  probably  prime  as follows.   
# Choose  10  random  numbersa1,a2,...,a10 between  2  and n−1 and  com-putean−1imodnfor eachai.
# Ifan−1i≡1 (modn)for any ai, return the message “n is composite.”   
# If an−1i≡1 (modn)for  all  the ai’s,  return  the  message  “n is probably prime.

#fermats theorem where if a ** n-1 = 1(mod n), n is prime, 
def fermats(n):
    randomlist = []
    for i in range(10):
        randomlist.append(random.randrange(2, n-1))
        i += 1
    for i in randomlist:
       if successivesquaring(i, n-1, n) != 1:
           return False
    return True



