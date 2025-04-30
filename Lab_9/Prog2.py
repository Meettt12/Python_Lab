def compute(n):
    sum=0
    for i in range(1,n+1):
        sum += int(str(n)*i)
        print('the n',sum)
    return sum
a = int(input('Enter the number :'))
print(compute(a))

    
