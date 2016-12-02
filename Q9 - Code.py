def binary (array, low, high):      #this will be the binary sequence and the intervals (low and high)
    while array:
        mid = len(array) // 2       #this will find the mid point of the array
        if array[mid] in range(low, high+1): #this checks if the mid of the array is inbetween the low and high points and will return true if it works         
            return True
        elif array[mid] < high: #this checks if the high interval is bigger than the mid      
            array = array[mid+1:]   #if it is it will make the array from mid+1
        elif array[mid] > low:          #this does the same but to see if mid is bigger than the low point
            array = array[0:mid]    #if it is it will check from the start to mid
    return False
