#Write a program that merges lines alternatively from two files and writes the results
#to new file. If one file has less number of lines than the other,
#the remaining lines from the larger file should be simply copied into the target file.
f = open(r"C:\Users\rahul\OneDrive\Desktop\Book1.csv")
f1 = open(r"C:\Users\rahul\OneDrive\Desktop\Book3.csv")
f3 = open(r"C:\Users\rahul\OneDrive\Desktop\Book4.csv","w+")
lines1 = f.readlines()
lines2 = f1.readlines()
max_len = max(len(lines1),len(lines2))
for i in range(max_len):
    if i < len(lines1):
        f3.write(lines1[i])
    if i < len(lines2):
        f3.write(lines2[i])
f.close()
f1.close()
f3.close()
