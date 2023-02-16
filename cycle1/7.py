li1=[]
li2=[]
sum1=sum2=flag=0
n1 = input("Size of list one : ")
for i in range(0,n1):
	li1.append(int(input("Enter list one elements: ")))
	sum1=sum1+li1[i]
n2 = input("size of list two : ")
for i in range(0,n2):
	li2.append(int(input("Enter list two elements : ")))
	sum2=sum2+li2[i]
l1 = len(li1)
l2 = len(li2)
if l1==l2:
	print"Same length :",l1
else:
	print"Diffrent length!!!!!!!"
if sum1==sum2:
	print"Sums are equal :",sum1
else:
	print"Sums are not equal!!!!!!1"


def same(li1,li2):
	r=0
	for i in range(0,n2):
		for j in range(0,n2):
			if li1[i]==li2[j]:
				r=1
				return r
	return r

p=same(li1,li2)
print(p)
