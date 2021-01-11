import random
import time

#start_time = time.time()

#The method of successive squaring described in the text allows you to compute a**k(mod m)quite  efficiently,  
# but it  does  involve  creating  a  table  of  powers  of a modulo m
#form: a^k(mod m)
def successivesquaring(a, k, m):
    b = 1
    while k >= 1:
        if k%2 != 0: #if k is odd
            b = (a * b) % m
        a = (a*a) % m
        k = k//2
    return b

#print(time.time() - start_time)

#Write a  program  to  check  if  a  number n is  composite  or  probably  prime  as follows.   
# Choose  10  random  numbersa1,a2,...,a10 between  2  and n−1 and  com-putean−1imodnfor eachai.
# Ifan−1i≡1 (modn)for any ai, return the message “n is composite.”   
# If an−1i≡1 (modn)for  all  the ai’s,  return  the  message  “n is probably prime.

def fermats(n):
    """
    #fermats theorem where if a ** n-1 = 1(mod n), n is prime,
    """
    randomlist = []
    for i in range(10):
        randomlist.append(random.randrange(2, n-1))
        i += 1
    for i in randomlist:
       if successivesquaring(i, n-1, n) != 1:
           return("n is composite")
    return("n is probably prime")
