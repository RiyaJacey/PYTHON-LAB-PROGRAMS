x = int(input("enter the first number"))
y = int(input("enter the second number"))
i=1
while((i<=x) and (i<=y)):
    i=i+1
    if (x % i == 0 and y % i == 0):
        gcd=i
print(gcd)
