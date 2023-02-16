def merge(a,b):
	res = {**a, **b}
	return res

d1 = {'a':21,'l':18,'p':3,'m':5}
d2 = {'r':5,'t':9}
d3 = merge(d1,d2)
print("Merged dictoinary : ",d3)
