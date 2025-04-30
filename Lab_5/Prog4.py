#List

import random
def List():
    lst=[]
    for i in range(30):
        lst.append(random.randint(-100,100))
    print(lst)
    p=[]
    n=[]
    for i in lst:
        if i>0:
            p.append(i)
        else:
            n.append(i)
    print(p,n)
List()
