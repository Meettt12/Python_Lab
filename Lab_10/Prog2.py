f= open("Book1.csv")
empty_dictionary = {}
data = f.readlines()
print('The readlines is',data,'\n')
filter = [lines.strip().split(',') for lines in data]
print('The fileter is ',filter,'\n')
for i in range(len(data)):
    empty_dictionary[filter[0][i]] = [x[i] for x in filter[1:]]
    
print(empty_dictionary)

