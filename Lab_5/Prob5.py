#List

def List():
    strings = ["hello", "world", "python", "code"]
    for i in range(len(strings)):
        strings[i] = strings[i].upper()
    print(strings)


List()
