area_square = lambda side : side * side
area_rectangle = lambda length,width : length * width
area_triangle =  lambda h,b : (h*b)*0.5
s = int(input("enter side of square: "))
a = int(input("length of rectange : "))
b = int(input("Width of rectangle : "))
h = int(input("height of triangle : "))
tb = int(input("base of triangle : "))
print("RESULT !!!!!")
print("Area of square : ",area_square(s))
print("Area of rectangle : ",area_rectangle(a,b))
print("Area of triangle : ",area_triangle(h,tb))
