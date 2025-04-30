# write a recursion program for prime factor of positive number
def prime(n,diviser = 2,factor = None):
    fact = []
    if n == factor:
        return fact
    if n<= 1:
        return fact
    if n%diviser == 0:
        fact.append(diviser)
        return prime(n//diviser,diviser,factor)
    else:
        return prime(n,diviser+1,factor)
n = int(input('Enter the number :'))
print(prime(n))


