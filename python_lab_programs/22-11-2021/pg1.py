print("print leap years between current to a final year entered by the user")
a=int(input("enter the current year"))
b=int(input("enter the final year"))
print("future leap years:")
for year in range(a, b):
    if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(year)