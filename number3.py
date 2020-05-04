#Given a number count the total number of digits in a number#
n = int(input("Enter a number to calculate the no of digits"))
c = 0
while(n > 0):
    c=(c+1)
    n=(n//10)
print("The number of digits in the given number are :",c)