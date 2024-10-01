n = int(input("Enter number: "))
reversed_num = 0
while n > 0:
    r = n % 10
    n = n // 10
    reversed_num = reversed_num * 10 + r
print("Reversed number:", reversed_num)