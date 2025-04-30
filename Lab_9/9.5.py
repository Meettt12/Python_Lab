def ispangram(str):
    str = str.lower()
    s= set(str)
    if (len(s)-1) == 26:
        print('The given string is "Pangram"')
    else:
        print('The given string is not "Pangram"')
str=input('Enter the string :')
ispangram(str)        
        
            
                
                
    
