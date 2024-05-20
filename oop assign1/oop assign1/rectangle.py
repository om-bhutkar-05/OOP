class rectangle:
    
     def __init__(self):
       self.len=0
       self.bre=0

     def area(self):
          print("The Area Of Rectangle is : ",self.len*self.bre)
     def perimeter(self):
          print("The Perimeter Of Rectangle is : ",2*(self.len+self.bre))
     def changedimension(self,len1,bre1):
          self.len=len1
          self.bre=bre1
     def reportdimension(self):
          print("The length of rectangle is : ",self.len)
          print("The breadth of rectangle is : ",self.bre)
       

r1=rectangle()
i=None
while(i != "0"):
     print("1. Area of rectangle \n2.perimeter of rectangle \n3.Change dimensions \n4.report dimensions \n5.0 to exit")
     i=input("Enter a choice: ")
     if(i=="1"):
          r1.area()
     elif(i=="2"):
          r1.perimeter()     
     elif(i=="3"):
          l=int(input("Enter the length of rectangle: "))
          b=int(input("Enter the breadth of rectangle: "))
          r1.changedimension(l,b)
     elif(i=="4"):
          r1.reportdimension()     
     

