#Write a function create_list()
#that creates and returns a list which is an intersection of two lists passed to it.
def create_list(l1,l2):
    s = l1+l2
    s = list(set(s))
    return s
l1 = [x for x in range(1,5)]
l2 = [y for y in range(2,9)]
print(create_list(l1,l2))
    
    
