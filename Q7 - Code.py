def is_prime(x):
    return check(x, x-1)

def check(n, k):
                    # your conditional check
    if n%k == 0:    #this works out if not a prime
        return False
    elif k == 2: #2 gets checked last 
        return True #will come back true if its a prime number
    else: 
        return check(n, k-1) #recursive calls it
