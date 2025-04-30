# Accept a year value from the user. Check whether it is a leap year or not.
def is_leap_year(year):
    return "Leap year" if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else "Not a leap year"

year = int(input("Enter a year: "))
print(is_leap_year(year))