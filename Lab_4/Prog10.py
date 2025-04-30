#Fibonaci Series

def Series():
    n = int(input("Enter the value of n: "))
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

Series()
