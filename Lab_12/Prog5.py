# Time 
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        self.minutes += self.seconds // 60
        self.seconds = self.seconds % 60
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
        self.hours = self.hours % 24

    def add(self, other):
        return Time(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

    def subtract(self, other):
        t1 = self.hours * 3600 + self.minutes * 60 + self.seconds
        t2 = other.hours * 3600 + other.minutes * 60 + other.seconds
        diff = abs(t1 - t2)
        return Time(diff // 3600, (diff % 3600) // 60, diff % 60)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

t1 = Time(2, 4, 15)
t2 = Time(1, 2, 5)
t3 = t1.add(t2)
t4 = t1.subtract(t2)
print("Time 1:", t1)
print("Time 2:", t2)
print("Added Time:", t3)
print("Subtracted Time:", t4)
print("Time 1 in seconds:", t1.to_seconds())

