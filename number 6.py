#write a python program to print fibonacci series and also check if a given input number is fibonacci number or not#
nterms = int(input("Enter number of terms to create Fibonacci series"))
n1,n2=0,1
c=0
if(nterms<=0):
    print("Enter a positive integer")
elif(nterms==1):
    print("Fibonacci sequence upto",nterm,"is-")
    print(n1)
else:
    print("Fibonacci sequence :")
    while(c<nterms):
        print (n1)
        n =n1+n2
        n1=n2
        n2=n
        c=c+1
#to check if a number is fibonacci number or not#
import math
def CheckperfectSquare(x):
    sqrt=int(math.sqrt(x))
    if pow(sqrt,2)==x:
        return True
    else:
        return False
    def isFiboNumber(x):
        res1=5*x*x +4
        res2=5*x*x -4
        if(CheckperfectSquare(res1) or CheckperfectSquare(res2)):
            return True
        else:
            return False
num = int(input("Enter an integer to check if a number is fibonacci or not"))
if(isFiboNumber(num)):
    print("Yes")
else:
    print("No")