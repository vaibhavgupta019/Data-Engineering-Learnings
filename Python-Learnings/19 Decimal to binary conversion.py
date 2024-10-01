dec = int(input("Enter decimal number: "))

bin = ''

while dec > 0:
    r = dec % 2
    dec = dec // 2
    bin = str(r) + bin

print("The corresponding binary is", bin)