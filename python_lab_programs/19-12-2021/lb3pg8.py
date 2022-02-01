string=input("enter the string:")
char=input("enter the character to count:")
count=0
for i in range(len(string)):
    if (string[i] == char):
        count = count + 1
print("The frequency of the ", char, "in the string is: ", count)