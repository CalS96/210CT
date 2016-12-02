import random
def shuffle(array):
    array1 = []             #Empty array where the new shuffled list will go

    while len(array) != 0:
        randomPos = random.randint(0, len(array)-1) #makes a random positon for an integer of the length of the list

        randomNum = array.pop(randomPos)        #pop will remove the object from the list
        array1.append(randomNum)            

    return array1

test1 = list(range(1,10))

print("test: {}".format(test1))     

shuffledArray = shuffle(test1)
print("shuffledArray: {}".format(shuffledArray))   #This tests the code and prints out an array and a shuffled array
