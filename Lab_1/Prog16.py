#Calculate interest where I = PRN/100.
P = float(input("Enter principal: "))
R = float(input("Enter rate: "))
N = float(input("Enter time: "))
interest = P * R * N / 100
print("Interest:", interest)
