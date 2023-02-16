li=[]
str=input("enter string : ")
print(str)
li=list(str)
print(li[0])
for i in range(1,len(li)):
    if li[i]==li[0]:
        li[i]='$'
print(li[:])