def fact(n):
	if n<0:
		print("Factorial = 0")
	elif n == 0 or n == 1:
		print("Factorial = 1")
	else:
		f=1
		while(n>1):
			f = f*n
			n = n-1
		print("Factorial = ", f)

n=int(input("Enter number : "))
fact(n)
