str = input("Enter string : ")
n=len(str)
d=n-3
if n>2:
	if str[d:] == 'ing':
		str = str + 'ly'
	else:
		str = str + 'ing'
	print(str)
else:
	print("Less than 3 characters are present !!!!!")
