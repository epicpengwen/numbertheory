value = int(input("Give a range: "))
def equation(rge):
    for i in range(1, rge):
        for j in range(1, rge):
            for k in range(1, rge):
                if((i*j)**3 + (j*k)**3 == (k*k)**2):
                    print(i)
                    print(j)
                    print(k)
                    print(i*j, j*k, k*k)
                    print((i*j)**3, (j*k)**3, (k*k)**2)

equation(value)