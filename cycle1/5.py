l=[]
n=int(input("size"))
print("enter element")
for i in range(0,n):
	l.append(int(input()))
for i in range(0,n):
	if l[i] > 100 : l[i] = 'over'
print(l[:])
