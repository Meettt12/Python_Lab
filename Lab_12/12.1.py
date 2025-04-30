#1. Write a program to create a class that represents Complex numbers containing real and
#imaginary parts and then use it to perform complex number addition, subtraction,
#multiplication and division

class myComplex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def printComplex(self):
        print(f'the complex is {self.real}+j{self.imag}')
    def Add(self,obj2):
       r = self.real + obj2.real
       i = self.imag + obj2.imag
       print(f'the Addition is {r}+j{i}')
    def Sub(self,obj2):
       r = self.real - obj2.real
       i = self.imag - obj2.imag
       print(f'the Substraction is {r}+j{i}')
    def Mul(self,obj2):
       r1= self.real*obj2.real
       i1 = self.imag*obj2.real
       r2= self.imag*obj2.imag
       i2 = self.real*obj2.imag
       print(f'the Multiplication is {r1-r2}+j{i1+i2}')
       return myComplex(r1-r2,i1+i2)
       
    def Conjugate(self):
        return myComplex(self.real,-self.imag)
    
    def Div(self,obj2):
        conj = obj2.Conjugate()
        numerator = self.Mul(conj)
        denominator = obj2.real**2 + obj2.imag**2
        result= myComplex(numerator.real/denominator,numerator.imag/denominator)
        print(f'the Division is {result.real}+{result.imag}j')
        return result
        
        
obj1 = myComplex(2,8)
obj2 = myComplex(7,3)
obj1.printComplex()
obj2.printComplex()
obj1.Add(obj2)
obj1.Sub(obj2)
obj1.Mul(obj2)
obj1.Div(obj2)

