# largest and smallest out of three

def ls3():
    a = float (input("Enter First Number :"))
    b = float (input("Enter Second Number :"))
    c = float (input("Enter Third Number :"))

    if a > b > c :
        print(a,">",b,">",c)
    elif a > c > b :
        print(a,">",c,">",b)
    elif b > a > c :
        print(b,">",a,">",c)
    elif b > c > a :
        print(a,">",c,">",b)
    elif c > b > a :
        print(c,">",b,">",a)
    elif c > a > b :
        print(c,">",a,">",b)

ls3()
ls3()
