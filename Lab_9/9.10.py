#Write a program that defines a function called frequency()
#which computes the frequency of words present in a string passed to it.
#The frequencies should be returned in sorted order of words in the string.
def frequency(str):
    words = str.lower().split()
    word_count = {}  

    for word in words:
        clean_word = "".join(char for char in word if char.isalnum())
        if clean_word:
            if clean_word in word_count:
                word_count[clean_word] += 1 
            else:
                word_count[clean_word] = 1

    return dict(sorted(word_count.items()))
s = input('Enter the string :')
print(frequency(s))
