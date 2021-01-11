#Write a program that takes as input a positive integer m and a polynomialf(X)
# having integer coefficients and produces as output 
# all of the solutions to the congruence f(X)≡0 (modm)

def polynomial(m):
    for i in range(0, m-1):
        if ((i**4 + 5*i**3 + 4*i**2 - 6*i - 4) % m ==0): #insert function
            print(i)
polynomial(11)