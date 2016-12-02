VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U") 
def vowelRemoval(aString):
    if len(aString) == 0:   #if there is nothing in the string
        return aString      # it returns the string
    else:
        newString = aString[1:len(aString) + 1]   #this will go through each letter of the string
        firstLetter = aString[0]
        
        if firstLetter in VOWELS:               #this checks the vowels

            return vowelRemoval(newString)
        else:
            return firstLetter + vowelRemoval(newString)
