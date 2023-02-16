li = []
s = 0
n = int(input("Enter size : "))
print("Enter",n,"elements")
for i in range(0,n):
	li.append(int(input("->")))
print("Elements in list : ",li)
for i in li:
	s = s+i
print("Sum : ",s)
