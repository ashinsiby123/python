#using built in function - line(2-12)
str1 = input("enter string 1 : ")
str2 = input("enter string 2 : ")
#desired output
# ->str1 = pbc
# ->str2 = aqr
x=str1[0:1]
print(x)
print(str2[0:1])
str1 = str1.replace(x,str2[0:1])
str2 = str2.replace(str2[0:1],x)
print("after swap : ",str1,str2)

#without function
"""str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
x = str2[:1] + str1[1:]
y = str1[:1] + str2[1:]
print("after swap : ",x,y)"""
