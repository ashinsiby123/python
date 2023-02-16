n = int(input("Number of words : "))
li=[]
l=0
for i in range(0,n):
	li.append(input("enter words : "))
for i in li:
	d=len(i)
	if d>l:
		l=d
print("Longest word -> ",i,"\nLength -> ",l)
