n = int(input("Enter number: "))
original_num = n
reversed_num = 0
while n > 0:
    r = n % 10
    n = n // 10
    reversed_num = reversed_num * 10 + r

if reversed_num == original_num:
    print("It is a PALINDROME")
else:
    print("It is NOT a PALINDROME!")