#Using built in function!!-line(3-5)

"""li1=set(['red','green','yellow'])
li2=set(['green'])
print(li1.difference(li2))"""

#Manually

li1 = []
li2 = []
n1 = int(input("Enter limit 1 : "))
for i in range(0,n1):
	li1.append(input("enter elements : "))

n2 = int(input("Enter limit 2 : "))
for i in range(0,n2):
	li2.append(input("Enter elements : "))

li3 = []
for i in li1:
	if i not in li2:
		li3.append(i)
print(li3)
