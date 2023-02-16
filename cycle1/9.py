str=input("enter string")
li=[]
li=list(str)
n=len(str)
temp=li[n-1]
li[n-1]=li[0]
li[0]=temp
print(li[:])