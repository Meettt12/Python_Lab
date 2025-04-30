#1. Write a program to create a class that represents Complex numbers containing real and
#imaginary parts and then use it to perform complex number addition, subtraction,
#multiplication and division
class myComplex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def printComplex(self):
        print(f'the complex is {self.real}+j{self.imag}')

    def __add__(self,obj2):
        return myComplex(self.real+obj2.real,self.imag+obj2.imag)
    def __sub__(self,obj2):
        return myComplex(self.real-obj2.real,self.imag-obj2.imag)
    def __mul__(self,obj2):
        r = self.real*obj2.real - self.imag*obj2.imag
        i = self.imag*obj2.real + self.real*obj2.imag
        return myComplex(r,i)
    def conjugate(self):
        return myComplex(self.real,-self.imag)
    def __truediv__(self,obj2):
        conj = obj2.conjugate()
        numerator = self*obj2
        denominator = self.real**2 + self.imag**2
        result = myComplex(numerator.real/denominator,numerator.imag/denominator)
        return result

obj1 = myComplex(2,8)
obj2 = myComplex(7,3)
obj1.printComplex()
obj2.printComplex()
print(f'{(obj1-obj2).real}+j{(obj1-obj2).imag}')
print(f'{(obj1+obj2).real}+j{(obj1+obj2).imag}')
print(f'The Multiplication is {(obj1*obj2).real}+j{(obj1*obj2).imag}')
print(f'The Division is {(obj1/obj2).real}+j{(obj1/obj2).imag}')

