def words(str):
#Function declaration that accepts a series of strings as an argument.
    cnt = dict() 
    """
    Creating an empty dictionary data type, to hold the string
    and the integer (The number of occurences as a pair). 
    """
    word = str.split()  
    #The split() function will take each string in the series as a separate entity.
     
   #Analysis of each character in a string.
    for char in word:  
        if char in cnt:  
            cnt[char] += 1 

        else:  
            cnt[char] = 1  
  
    return cnt  
  
print( words('olly olly : ¿Qué   in come free.')) 
#Function call
