# Calculate net salary 
# where net salary = gross salary + allowance – deduction.
# Allowances are 10% while deductions are 3% of gross salary.
g = float(input("Enter gross salary: "))
a = g * 0.10
d = g * 0.03
n = g + a - d
print("Net Salary:", n)
