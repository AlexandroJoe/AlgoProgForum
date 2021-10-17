import math

a = eval(input("Enter the numerator : Value must be greater than 0: "))

while a < 1:
    a = eval(input("Enter valid numerator : Value must be greater than 0: "))
else:
    b = eval(input("Enter the denominator : Value must be greater than 0: "))
    while b < 1:
        b = eval(input("Enter valid denominator : Value must be greater than 0: "))
    
c = math.gcd(a,b)
if a < b:
   print(a, '/', b, "is a proper fraction") 
   if c != 1 :
    print("This proper fraction can be reduced to: ", a//c, '/', b//c )
   else:
    print("This proper fraction cannot be reduced any futher")
elif a > b:
    print(a, '/', b, "is an improper fraction")
    if c == 1 :
        print("This improper fraction cannot be reduced any further")
        if a / b == a:
            print("The whole number is", a)
        else:
            print("The mixed number is", a//b, "and", a//c - a//b * b//c, '/',b//c)
    else:
        print("This improper fraction can be reduced to: ", a//c, '/', b//c)
        if a % b == 0:
            print("The whole number is", a//b)
        else:
            print("The mixed number is", a//b, "and", a//c - a//b * b//c, '/', b//c)

    