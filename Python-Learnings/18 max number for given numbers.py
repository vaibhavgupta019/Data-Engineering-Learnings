no_of_numbers = int(input("Enter number count: "))
counter = 0

max = int(input("Enter number: "))
while counter < no_of_numbers - 1:
    n = int(input("Enter number: "))
    if n > max:
        max = n
    counter = counter + 1

print("Max number:",max)