li=[]
n=int(input("limit : "))
for i in range(0,n):
	li.append(int(input("Enter elements")))
print("Orginal list : ",li)
li2=[]
for i in li:
	if i%2 != 0:
		li2.append(i)
print("List without even numbers : ",li2)
