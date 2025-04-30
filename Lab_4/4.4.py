n = int(input('Enter the number : '))

def prime():
    if n%2==0:
        print('The number is Co-Prime..')
    else:
        for i in range(3,int(n**0.5),2):
            if n%i==0:
                print('The number is Prime..')
                break
            else:
                print('The number is Co-Prime..')
                break
prime()
def perfect():
    a=0
    for i in range(1,n):
        if n%i==0:
            a=a+i
            if a==n:
                print('The number is Perfect..')
                break
        else:
            print('The number is not Perfect')
            break
perfect()
def armstrong():
    n_stri=str(n)
    n_digi=int(n)
    pow_sum=0
    for i in n_stri:
        num=int(i)**3
        pow_sum=pow_sum+num
    if pow_sum==n_digi:
        print('The number is Armstrong..')
    else:
        print('The number is not Armstrong..')
    
    
armstrong()
def prlidrom():
    n_str=str(n)
    if n_str == n_str[::-1]:
        print('The number is Palidrome..')
    else:
        print('The number is not Palidrome..')
            
prlidrom()

def automophic():
    pow_num=str(n**2)
    n_str=str(n)
    if pow_num[-len(n_str):] == n_str:
        print('The number is Automorphic..')
    else:
        print('The number is not Automorphic..')
        
automophic()