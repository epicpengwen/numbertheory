#euclidean algorithm for returning greatest common divisor of two numbers

#firstnum = int(input("First number:"))
#secondnum = int(input("Second number:"))

def euclidean(first, second):
    if(second > first):
        temp = first
        first = second
        second = temp
    remainder = second
    while(remainder != 0):
        remainder = first % second
        first = second
        second = remainder
        #print(first, second)
    return first

#print(euclidean(firstnum, secondnum))
