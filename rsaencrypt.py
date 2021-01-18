import math
import random
from euclideanalgorithm import euclidean
import textwrap
from succsqu import successivesquaring

def encrypt(message):
    """
    encrypts a message from the user using rsa returning a list of numbers
    method:
    1. choose two large prime numbers between 10,000 and 20,000
    """
    
    #convert message into  string of numbers
    #replace all punctuation with space
    levi = []
    armin = message.upper()
    for symbol in armin:
        if symbol in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            levi.append(symbol)
    print(levi)
    #create dict of letters associated with 2 digit numbers
    mikasa = {'A':11, 'B':12, 'C':13, 'D':14, 'E':15, 'F':16, 'G':17, 'H':18, 'I':19, 'J':20, 'K':21, 'L':22, 'M':23, 'N':24, 'O':25, 'P':26, 'Q':27, 'R':28, 'S':29, 'T':30, 'U':31, 'V':32, 'W':33, 'X':34, 'Y':35, 'Z':36}

    #every letter replaced with corresponding number to create a string of numbers
    sasha = ""
    for letter in levi:
        sasha += str(mikasa[letter])

    #choose two large prime numbers
    b = random.randrange(10000, 200000)
    while isPrime(b) == False:
        b = random.randrange(10000, 200000)
    r = random.randrange(10000, 200000)
    while isPrime(r) == False:
        r = random.randrange(10000, 200000)
    
    m = r * b
    print("m : ", m)

    mphi = (r-1)*(b-1)
    #check that mphi and k are relatively prime using euclidean algorithm
    k = random.randrange(10000, 100000) 
    while euclidean(k, mphi) != 1:
        k = random.randrange(10000, 100000)
    print("k : ", k)

    #split string of numbers into segments as long as the number m - 1
    krista = len(str(m))
    jean = textwrap.wrap(sasha, krista - 1)


    #now we have two primes and k and a list
    #use successive squaring to raise each of these numbers to the kth power modulo m
    connie = []
    for num in jean:
        connie.append(successivesquaring(int(num), k, m))

    return connie
    

def isPrime(n):
    if n % 2 == 0:
        return False
    k = 3
    while k*k <= n:
        if n % k == 0:
            return False
        k += 2
    return True

if __name__ == '__main__':
    eren = input("Enter message : ")
    print(encrypt(eren))
