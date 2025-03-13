length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

class Rectangle :
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        Area = self.length * self.width
        print(f"The area of the recangle is {Area}")
        
    def perimeter(self):
        per = 2 *(self.length + self.width)
        print(f"The perimeter of the recangle is {per}")

myrectangle = Rectangle(length,width)
myrectangle.area()
myrectangle.perimeter()