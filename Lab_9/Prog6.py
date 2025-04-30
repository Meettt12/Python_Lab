#    Function

def ispalidrom(str):
    reversed_s = "".join(reversed(str)).lower()
    s = ''.join(str).lower()
    cleaned_revers_s = "".join(char for char in reversed_s if char.isalnum())
    cleaned_s = "".join(char for char in s if char.isalnum())


    if cleaned_s== cleaned_revers_s:
        print('The string is palidrom')
    else :
        print('The string is not palidrom')
str = input('Enter the string :')
ispalidrom(str)


    
