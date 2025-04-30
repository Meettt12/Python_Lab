#List

import random
def List():
    lst=[]
    for i in range(50):
        lst.append(random.randint(1,30))
    print(lst)
    l=[]
    for i in lst:
        if i not in l:
            l.append(i)
    print(l)

List()
