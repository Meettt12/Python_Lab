class String:
    def __init__(self,string):
        self.string=string
    def __iadd__(self,other):
        self.string += other.string
        return self
    def toLower(self):
        return self.string.lower()
    def toUpper(self):
        return self.string.upper()
    def display(self):
        return self.string
s1=String("roniitt")
s2=String("RROONNIIITTT")
s1+=s2
upperCase=s1.toUpper()    
lowerCase=s2.toLower()    
print("s1+=s2",s1.display())
print(upperCase)
print(lowerCase)
