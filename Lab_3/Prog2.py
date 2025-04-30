def lower():
    str=input('Enter a string :')
    str1=''
    for ch in str:
        if ch>='A' and ch<='Z':
            str1=str1+chr(ord(ch)+32)
        else:
            str1=str1+ch
    return str1
def toggle():
    str=input('Enter a string :')
    str1=''
    for ch in str:
        if ch>='A' and ch<='Z':
            str1=str1+chr(ord(ch)+32)
        elif ch>='a' and ch<='z':
            str1=str1+chr(ord(ch)-32)
        else:
            str1=str1+ch
    return str1

print(lower())
print(toggle())

