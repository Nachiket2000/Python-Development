#program to accept 2 numbersfrom a user and return their product and if the product is greater than 1000,then return their sum#
a = int(input("Enter first integer \n "))
b = int(input("Enter the second integer \n"))
c = a*b
if c>1000:
    print(a+b)
else:
    print(c)