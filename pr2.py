def circle(r):
    pi = 3.14
    area = r*r*pi
    return area

n = int(input("enter a radius of circle: "))
circlearea = circle(n)
print("Area of the circle is:",circlearea)

class parrot:
    name = ""
    age = 0

p1 = parrot()
p1.name = "bluu"
p1.age = 10

print(f"{p1.name} is {p1.age} old name")

class Room:
    length = 0
    breath = 0

    def calculate(self):
        print("Area of room : ",self.length * self.breath)

study = Room()
study.length = 100
study.breath = 0.1
study.calculate()
