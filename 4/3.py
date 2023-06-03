class Rectangle:
    def __init__(self, length, width) -> None:
        self.l = length
        self.w = width

    def area(self):
        return self.l * self.w
    def perimeter(self):
        return 2 * (self.l + self.w)


rec1 = Rectangle(length=20, width=15)
print(f"the rectangle area is: {rec1.area()}")
print(f"the perimeter area is: {rec1.perimeter()}")

