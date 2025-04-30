#Write a program that defines a function convert() that receives a string containing
#a sequence of whitespace separated words and returns a string after removing all
#duplicate words and sorting them alphanumerically.
#Hint: use set(), list () , sorted(), join()
def convert(s):
    st = str(set(s))
    st = sorted(st)
    final_str = ''.join(char for char in st if char.isalnum())
    return final_str
s = input('Enter the string :')
print(convert(s))
    
