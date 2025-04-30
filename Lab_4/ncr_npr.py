n = int(input('Enter the value of n : '))
r = int(input('Enter the value of r : '))
def factorial(a):
    fct=1
    for i in range(1,a+1):
        fct=fct*i
    return fct
def ncr():
    ncr=factorial(n)/(factorial(n-r)*factorial(r))
    print('The ncr :',ncr)
    
ncr()
def npr():
    npr=factorial(n)/factorial(n-r)
    print('The npr :',npr)
    
npr()
        