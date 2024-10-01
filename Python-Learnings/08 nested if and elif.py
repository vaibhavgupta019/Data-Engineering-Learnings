john = float(input("Enter John's age: "))
smith = float(input("Enter Smith's age: "))
ajay = float(input("Enter Ajay's age: "))

if john > smith and john > ajay:
    print("John is eldest")
else:
    if smith > ajay:
        print("Smith is eldest")
    else:
        print("Ajay is eldest")
'''
if john > smith and john > ajay:
    print("John is eldest")
elif smith > ajay:
    print("Smith is eldest")
else:
    print("Ajay is eldest")
'''