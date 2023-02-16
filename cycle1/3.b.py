a=[]
n=int(input("Number of elements : "))
print("Enter elements : ")
for i in range(0,n):
	a.append(int(input()))
r=[i*i for i in a]
print("Squares are : ", r)