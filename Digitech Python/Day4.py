# This programe checks on the user input and validate it
print("This programe needs the credentials to verify them to grant access to users")
print()
# username = "Phoenix"
# password = "Phoenix6789"
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "Phoenix" and password == "Phoenix6789":
    print("Signed in successfully!")

elif username != "Phoenix" and password == "Phoenix6789":
    print("Check your credentials and try again!")

else:
    print("Wrong credentials")