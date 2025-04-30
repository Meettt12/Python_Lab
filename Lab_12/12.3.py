#Write a program to create a class that can calculate the surface area and volume of a solid.
#The class should also have a provision to accept the data relevant to the solid.
class Solid:
    def __init__(self,l,w,h):
        self.l = l
        self.w = w
        self.h = h
    def GetSolid(self):
        self.l = int(input('Enter the Length of Solid :'))
        self.w = int(input('Enter the Width of Solid :'))
        self.h = int(input('Enter the Height of Solid :'))
    def Volume(self):
        return self.l*self.w*self.h
    def Area(self):
        return 2*(self.l*self.w + self.w*self.h+self.h*self.l)
obj1=Solid(0,0,0)
obj1.GetSolid()
print('The Volume is',obj1.Volume())
print('The Area is',obj1.Area())
    
