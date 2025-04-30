
def factorial():
    n = int(input('Enter the number : '))
    fct=1
    for i in range(1,n+1):
        fct=fct*i
    print('The Factorial :',fct)

factorial()