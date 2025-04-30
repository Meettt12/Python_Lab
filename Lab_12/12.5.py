#Write a program that creates and uses a
#Time class to perform various time arithmetic operations.
class time:
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s
    def __add__(self,t2):
        hour = self.h + t2.h
        minut = self.m + t2.m
        second = self.s + t2.s
        if second>=60:
            minut+=1
            second -=60
        if minut >=60:
            hour+=1
            minut -=60
        return time(hour,minut,second)
    def __sub__(self,t2):
        hour = self.h - t2.h
        minut = self.m - t2.m
        second = self.s - t2.s
        if second<0:
            minut-=1
            second +=60
        if minut<0:
            hour-=1
            minut+=60
        return time(hour,minut,second)
    def __str__(self):
        return f'{self.h :02d}:{self.m :02d}:{self.s :02d}'
    def __del__(self):
        print('The objects are deleted..')

t1 = time(4,23,45)
print('T1',t1)
t2 = time(2,42,17)
print('T2',t2)
print("T1 + T2",t1+t2)
print("T1 - T2",t1-t2)
