#Write a program to copy contents of one file to another.
#While doing so, replace all lowercase characters into uppercase characters.
f = open(r"C:\Users\rahul\OneDrive\Desktop\Book1.csv")
f1 = open(r"C:\Users\rahul\OneDrive\Desktop\Book3.csv","w+")
for line in f:
    print(line)
    f1.write(line.upper())
f.close()
f1.close()
