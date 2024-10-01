# To check if marks of a subject are within range 0 - 100
marks = float(input("Enter marks of a subject: "))

if marks >= 0 and marks <= 100:
    print("Valid marks")
else:
    print("Invalid")