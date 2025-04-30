# Methods 

class String:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other.value
        return self

    def toLower(self):
        self.value = self.value.lower()

    def toUpper(self):
        self.value = self.value.upper()

    def __str__(self):
        return self.value

s1=String("Meet")
s2=String("MEET")
s1+=s2
upperCase=s1.toUpper()    
lowerCase=s2.toLower()    
print("s1+=s2",s1.display())
print(upperCase)
print(lowerCase)
