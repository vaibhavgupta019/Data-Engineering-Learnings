year = int(input("Enter Year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not a leap year")