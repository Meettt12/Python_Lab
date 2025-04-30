# Files

f= open("Excel1.csv")
empty_dictionary = {}
data = f.readlines()
print('The Readlines Is',data,'\n')
filter = [lines.strip().split(',') for lines in data]
print('The Fileter Is ',filter,'\n')
for i in range(len(data)):
    empty_dictionary[filter[0][i]] = [x[i] for x in filter[1:]]
    
print(empty_dictionary)

