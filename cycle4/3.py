class Rectangle:
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth
	
	def cal_area(self):
		self.area = self.length * self.breadth
		print(self.area)
	
	def __it__(self,second):
		if self.area < second.area:
			return True
		else:
			return False

print("Enter lenth and breadth of rectangle 1 : ")
l,b = int(input()),int(input())
print("Enter lenth and breadth of rectangle 2 : ")
l2,b2 = int(input()),int(input())

print("Rectangle 1 area : ")
r = Rectangle(l,b)
r.cal_area()

print("Rectangle 2 area : ")
r2 = Rectangle(l2,b2)
r2.cal_area()

if r < r2:
	print("Rectangle 2 is large")
else:
	print("Rectangle 1 is larger or these are equal") 
