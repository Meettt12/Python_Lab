def apb(a,b):
    if b == 0:
        return 1
    else:
        return a*(apb(a,b-1))
print(apb(2,3))