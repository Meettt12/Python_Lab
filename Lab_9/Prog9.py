#Write a program that defines a function count_alpha_digits()
#that accepts a string and calculates the number of alphabets and digits in it.
#It should return these values as a dictionar
def count_alpha_digits(str):
    count_alpha = 0
    count_digit = 0
    for ele in str:
        if ele.isalpha():
            count_alpha +=1
        elif ele.isdigit():
            count_digit +=1
        ans = {'Alphabets' : count_alpha,'Digits':count_digit}
    return ans
s = input('Enter the string containg alphabets and numbers :')
print(count_alpha_digits(s))
    
