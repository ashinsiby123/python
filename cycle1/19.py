def gcd(a, b):
    # Find minimum of a and b
    result = min(a, b)
    while result:
        if a % result == 0 and b % result == 0:
            break
        result = result  - 1
    # Return the gcd of a and b
    return result

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
d = gcd(a,b)
print("GCD of",a,"and",b,"is : ",d)
