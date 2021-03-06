import math
from eulers_phi import unique, phi_function
from leq import linu, solve_Dioph
from succsqu import successivesquaring

#RSA public key cryptosystem

#takes m, k

def decrypt(m, k, pikachu):
    """
    RSA decryption taking p, q, and k values to decode a list of numbers and return a message
    """
    #create empty string for list of digits to be added to
    Answer = ''
    message = ''

    #iterate through list of numbers and apply chapter 17 methods to solve congruences 
    for number in pikachu:
        Answer += str(kroots(k, number, m))

    #create dict of letters associated with 2 digit numbers
    #create for loop for this?
    ash = {11:'A', 12:'B', 13:'C', 14:'D', 15:'E', 16:'F', 17:'G', 18:'H', 19:'I', 20:'J', 21:'K', 22:'L', 23:'M', 24:'N', 25:'O', 26:'P', 27:'Q', 28:'R', 29:'S', 30:'T', 31:'U', 32:'V', 33:'W', 34:'X', 35:'Y', 36:'Z'}

    #iterate through string of digits by twos to convert into legible message
    for i in range(0, len(Answer), 2):
        if int(Answer[i:i+2]) > 36 or int(Answer[i:i+2]) < 11:
            message += "%"
        else:
            message += ash[int(Answer[i:i+2])]

    return(message)

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
    
    mphi = phi_function(m)
    #print(mphi)
    #linear equation ku - phiv = 1
    #u = linu(k, mphi)
    u = solve_Dioph(k, (-1 * mphi), 1)

    #successivesquaring
    return(successivesquaring(b, u, m))
    
if __name__ == '__main__':
    userlist = [int(item) for item in input("Enter the list of numbers : ").split(", ")]
    m = int(input("Enter your value for m: "))
    k = int(input("Enter your value for k: "))

    print(decrypt(m, k, userlist))