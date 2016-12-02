def reverse_sentence(p):
    reverseSentenced = " "
    string = " "
    for char in p: #for characters in p
        if char != " ": #If characters dont equal an empty string
            string += char #this modifys the object in place as it is mutable
        else:
            reverseSentenced = string + " " + reverseSentenced
            string = " "

    reverseSentenced = string + " " + reverseSentenced
    p = reverseSentenced
    return p
    
    
