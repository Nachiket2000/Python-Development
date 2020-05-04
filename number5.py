#Write a python program to print all the prime number in a given interval and also check is a given input number is prime or not#
lower = int(input("Enter the lower range "))
upper = int(input("Enter the upper range "))
for num in range(lower,upper+1):
    if (num>1):
        for i in range(2,num):
            if((num%i)==0):
                break
            else:
                print(num)
#to check a number is prime or not#
a = int(input("Enter a number to check if it is prime or not"))
b = 1
if(a > 1):
    for b in range (2,a):
        if ((a%b)==0):
            print(a,"is not a prime number")
            break
        else:
            print(a,"is prime")
else:
    print(a,"is not a prime number")


