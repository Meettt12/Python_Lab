def re():
    try:
        a=input('Enter the string:')
        b=input('Enter string to remove:')
        if b in a:
            d=a.replace(b,'')
        print(d)
    except:
        print('Invalid')

re()
