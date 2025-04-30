# Convert number 0 to 19 to its equivalent words. E.g. 0 -> zero, 19 -> nineteen.
def number_to_words(n):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    return words[n] if 0 <= n <= 19 else "Invalid input"

n = int(input("Enter a number (0-19): "))
print(number_to_words(n))