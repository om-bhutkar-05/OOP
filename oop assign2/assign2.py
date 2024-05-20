class polygon:
    def __init__(self,side):
        pass
    def perimeter(self):
        pass
    def area(self):
        pass
    def printv(self):   
        pass
    def change_d(self):
        pass

class square(polygon):
    per=None
    side=None
    ar=None
    def __init__(self,sides):
        self.side=0
    def perimeter(self):
        self.per=4*self.side
    def area(self):
        self.ar=self.side*self.side
    def printv(self):
        print("Sqaure:")
        print("The side of square is ",self.side)
        print("The area of square is ",self.ar)
        print("The area of perimeter is ",self.per)
    def change_d(self):
        self.side=int(input("Enter the side of a square:"))
class rectangle(polygon):
    per=None
    len=None
    bre=None
    ar=None
    def __init__(self,len,bre):
        self.len=0
        self.bre=0
    def perimeter(self):
        self.per=2*(self.len+self.bre)
    def area(self):
        self.ar=(self.len*self.bre)
    def printv(self):
        print("Rectangle:")
        print("The length  of rectangle is ",self.len,"\nThe breadth of rectangle is ",self.bre)
        print("The area of rectangle is ",self.ar)
        print("The perimeter of rectangle is ",self.per)
    def change_d(self):
        self.len=int(input("Enter the length of a rectangle:"))
        self.bre=int(input("Enter the breadth of a rectangle:"))
        

a=square(0)
b=rectangle(0,0)
a.area()
b.area()
a.perimeter()
b.perimeter()
a.printv()
b.printv()
a.change_d()
b.change_d()
a.area()
b.area()
a.perimeter()
b.perimeter()
a.printv()
b.printv()




