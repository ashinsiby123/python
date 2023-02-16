str = input("Enter string : ")
fre = {}

for i in str:
	if i in fre: 
		fre[i] = fre[i] + 1
	else:
		fre[i]=1
print(fre)
