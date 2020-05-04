#Accept a string from a user and display only those characters which are present at an even index number#
str1 = input("Enter a string \n ")
index = 0
while (index< len(str1)):
    print(str1[index],end='')
    index=index+2