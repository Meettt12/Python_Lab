def create_array(n):
    return [[[n for i in range(5)]for i in range(4)]for i in range(3)]

n = int(input('Enter the number : '))
print(create_array(n))
    
    
