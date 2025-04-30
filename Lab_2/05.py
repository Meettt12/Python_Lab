# Accept age of a person. If age is less than 18, print minor otherwise Major.
def check_age_category(age):
    return "Minor" if age < 18 else "Major"

age = int(input("Enter age: "))
print(check_age_category(age))