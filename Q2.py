def Trailing_Zeros(x):
    fives = 0 #sets counter for fives as there currently is no fives
    for number in range(2, x+1): #it starts from 2 up till what x is + 1 so no errors will occur        
        while number > 0:
            if number % 5 == 0:
                fives += 1  #if the number gets divided by 5 as a int and not a float it will add a 5 in the fives counter
                number = number/5
            else:
                break
    return fives   #returns the final result
