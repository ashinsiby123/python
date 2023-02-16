li = []
n=input("number")
for i in range(0,n):
	li.append(input("Enter first names : "))
count=0
for i in range(0,n):
	for j in range(0,len(li[i])):
		if li[i][j]=='a':
			count = count+1
print "Occurance of 'a' within the list : ", count
