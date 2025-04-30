def count_lower_upper(str):
    lwc = 0
    upc = 0
    for ele in str:
        if ele.isupper():
            upc+=1
        else :
            lwc+=1
    ans = {'Upper' : upc , "Lower" : lwc}
    return ans
str = input('Enter the strig : ')
print(count_lower_upper(str))
