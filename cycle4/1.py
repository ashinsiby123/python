class Rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b
		
	def area(self):
		self.ar=self.l*self.b
	
	def perimeter(self):
		self.pr=2*(self.l+self.b)
	
	def display(self):
		print("Area : ",self.ar)
		print("Perimeter : ",self.pr)
	
	def compare(self,p2):
		if self.ar == p2.ar:
			print("equal")
		elif self.ar > p2.ar:
			print("area1 is greater")
		else:
			print("area2 is greater")
		
l1=input("enter length 1 : ")
b1=input("enter breadth 1 : ")

l2=input("enter length 2 : ")
b2=input("enter breadth 2 : ")

p1=Rectangle(l1,b1)

p1.area()
p1.perimeter()
p1.display()

p2=Rectangle(l2,b2)

p2.area()
p2.perimeter()
p2.display()

p1.compare(p2)
