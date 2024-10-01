counter = int(input("How many numbers you want to add? "))
sum = 0

while counter > 0:
    n = int(input("Enter number: "))
    sum = sum + n
    counter = counter - 1

print("Sum of given numbers:",sum)