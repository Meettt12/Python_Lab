#Lower & Upper

def count_lower_upper(str):
    l = 0
    u = 0
    for ele in str:
        if ele.isupper():
            u+=1
        else :
            l+=1
    ans = {'Upper' : u , "Lower" : l}
    return ans
str = input('Enter the strig : ')
print(count_lower_upper(str))
