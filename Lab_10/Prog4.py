"""Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory."""


f = open(r"D:\College\Python\Lab10\Excel1.csv")
f1 = open(r"D:\College\Python\Lab10\Excel2.csv","w+")
for line in f:
    print(line)
    f1.write(line)
print(f1.read())
f.close()
f1.close()

