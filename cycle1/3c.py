str = input("enter string : ")
li = list(str)
vo = ['a','e','i','o','u','A','E','I','O','U']
print(li)
li2=[]
for i in li:
	if i in vo:
		li2.append(i)
print(li2)
