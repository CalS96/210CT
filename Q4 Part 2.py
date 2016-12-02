def Trailing_Zeros(x):
    fives = 0
    for number in range(2, x+1):            #O (n)         
        while number > 0:                   #O (n^2)
            if number % 5 == 0:             #O (n^2)
                fives += 1                  #O (n^2)
                number = number/5           #O (n^2)
            else:
                break
    return fives                            #O (1)

# The run time bounds of this function is 0 (n^2)
