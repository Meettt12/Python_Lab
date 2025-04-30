str=input('Enter the string : ')

def countAlphabate():
    countAlp=0
    countDig=0
    for ch in str:
        if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
            countAlp=countAlp+1

        else:
            countDig+=1

    print('The number of Alphabates are : ',countAlp)
    print('The number of Digits are : ',countDig)
    
countAlphabate()
