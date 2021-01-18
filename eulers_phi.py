import math

def unique(list1): 
    """
    condenses the list to unique solutions
    """
    # intilize a null list 
    unique_list = [] 

    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list


def phi_function(n):
    """
    Euler's phi function: factors into list of primes to find ...
    """
    
    listofsmallprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    factorlist = []
    #iterate through list of primes to check which factor into n, then adds to a factor list
    for i in listofsmallprimes:              
        while((n/i).is_integer()):
            factorlist.append(i)
            n = n//i
    for i in range(103, int(math.sqrt(n), 2)):   
        while((n/i).is_integer()):
            factorlist.append(i)
            n = n//i
    if (n != 1):
        factorlist.append(n)
    answer = 1
    factors = unique(factorlist)
    for i in factors:
        p = i
        k = factorlist.count(p)
        answer = answer * ((p**k) - (p**(k-1)))
    return(answer)
# print(phi_function(956331992007843552652604425031376690367))