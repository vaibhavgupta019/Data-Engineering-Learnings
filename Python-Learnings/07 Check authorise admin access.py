# john or smith is authorised for admin access. Check if a person is authorise for admin access.
username = input("Enter username: ")

if username == 'john' or username == 'smith':
    print("Authorised for ADMIN access")
else:
    print("Not authorised")