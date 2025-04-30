class Date:
    def __init__(self,date1):
        self.date1=date1
    def __eq__(self,other):
        for i in range(len(self.date1)):
            if self.date1[i]==other.date1[i]:
                continue
            else:
                return False
        return True
a=Date([20,10,12])
b=Date([20,11,12])
print(a==b) #false