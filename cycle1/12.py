import os
f=input("Enter file name")
# this will return a tuple of root and extension
s = os.path.splitext(f)
f_exte = s[1]
print("File Extension: ", f_exte)
