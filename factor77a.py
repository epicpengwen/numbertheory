import math

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
    print(factorlist)


#for i in range(1000000, 1000030):
factor_function(10923)