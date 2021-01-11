#loop thru until 3n+1, Start with any number n. If n is even, divide it by 2. If n is odd, replace it with 3n + 1. Repeat
#table?at bottom
def function(n):
    a = 0
    while n > 0:
        a += 1
        if (n == 1):
            break
        elif n%2 == 0:
            n = n / 2
            #print(n)
        else:
            n = 3*n + 1
            #print(n)
    print(a)
    

#function(5)
for i in range(1, 100):
    function(i)
    
        

