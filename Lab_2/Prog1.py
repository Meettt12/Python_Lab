#// smalllest and largest number

a = float(input("Enter Number : "))
b = float(input("Enter Another Number : "))

small = a if a < b else b
large = a if a > b else b

print("The Small Number Is : ", small)
print("The Small Number Is : ", large)
