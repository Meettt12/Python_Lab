#Create a specific subdirectory and copy
#one file from another subdirectory to this newly created subdirectory.
f = open(r"C:\Users\rahul\OneDrive\Desktop\Book1.csv")
f1 = open(r"C:\Users\rahul\OneDrive\Desktop\Book2.csv","w+")
for line in f:
    print(line)
    f1.write(line)
print(f1.read())
f.close()
f1.close()

