# Q4 - Big O notation
import random
def shuffle(array):
    array1 = []             

    while len(array) != 0:                              #O(n)
        randomPos = random.randint(0, len(array)-1)
        
        randomNum = array.pop(randomPos)                #O(n)       
        array1.append(randomNum)                        #O(n)           

    return array1                                       #O(n)

test1 = list(range(1,10))

print("test: {}".format(test1))

shuffledArray = shuffle(test1)
print("shuffledArray: {}".format(shuffledArray))

# The run time bounds of this function are 0(n)
