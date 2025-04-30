"""Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters."""


f = open(r"D:\College\Python\Lab10\Excel1.csv")
f1 = open(r"D:\College\Python\Lab10\Excel3.csv","w+")
for line in f:
    print(line)
    f1.write(line.upper())
f.close()
f1.close()
