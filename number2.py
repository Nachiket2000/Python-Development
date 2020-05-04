#program to accept "n" no. from an user and calculate sum of all numbers#
n = input("Enter number to calculate sum")
n = int(n)
sum=0
for num in range(0,n+1,1):
    sum=sum+num
    print("Sum of first",n,"numbers is :",sum)