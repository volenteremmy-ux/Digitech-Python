# # This programe checks on the user input and validate it
# print("This programe needs the credentials to verify them to grant access to users")
# print()
# # username = "Phoenix"
# # password = "Phoenix6789"
# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if username == "Phoenix" and password == "Phoenix6789":
#     print("Signed in successfully!")

# elif username != "Phoenix" and password == "Phoenix6789":
#     print("Check your credentials and try again!")

# else:
#     print("Wrong credentials")

# print("Welcome")

# #Access Control
# users = {
#     "Phoenix": "Phoenix6789",
#     "Admin": "Admin6789",
#     "Guest": "Guest1234"
# }

# # Maximum no. of login attempts
# max_attempts = 3
# attempts = 0

# while attempts < max_attempts:
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")

#     # Check if username exists and password matches
#     if username in users and users[username] == password:
#         print(f"Access granted! Welcome, {username}!")
#         break
#     else:
#         attempts += 1
#         print(f"Invalid credentials. {max_attempts - attempts} attempt(s) left.")

# # If attempts exceeded
# if attempts == max_attempts:
#     print("Access denied. Too many failed attempts!")

#Menu selection
print("Welcome to the Access Control System")

# # Users and passwords
# users = {
#     "Phoenix": "Phoenix6789",
#     "Admin": "Admin6789",
#     "Guest": "Guest1234"
# }

# max_attempts = 3
# attempts = 0
# logged_in_user = None 

# while attempts < max_attempts:
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")

#     if username in users and users[username] == password:
#         print(f"\nAccess granted! Welcome, {username}!\n")
#         logged_in_user = username
#         break
#     else:
#         attempts += 1
#         print(f"Invalid credentials. {max_attempts - attempts} attempt(s) left.\n")

# if logged_in_user is None:
#     print("\nAccess denied. Too many failed attempts!")
# else:
#     # Menu
#     while True:
#         print("Menu")
#         print("1. View Profile")
#         print("2. Change Password")
#         print("3. Logout")

#         choice = input("Enter your choice (1-3): ")

#         if choice == "1":
#             print(f"\nUsername: {logged_in_user}")
#             print("Status: Logged in successfully!\n")

#         elif choice == "2":
#             new_password = input("Enter new password: ")
#             users[logged_in_user] = new_password
#             print("Password changed successfully!\n")

#         elif choice == "3":
#             print(f"\nGoodbye, {logged_in_user}!\n")
#             break

#         else:
#             print("Invalid choice. Please try again.\n")


# Error handling
print("Welcome to the Access Control System\n")

users = {
    "Phoenix": "Phoenix6789",
    "Admin": "Admin6789",
    "Guest": "Guest1234"
}

max_attempts = 3
attempts = 0
logged_in_user = None

# Login
while attempts < max_attempts:
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Checking empty inputs
        if username.strip() == "" or password.strip() == "":
            raise ValueError("Username or password cannot be empty.")

        # Checking credentials
        if username in users and users[username] == password:
            print(f"\nAccess granted! Welcome, {username}!\n")
            logged_in_user = username
            break
        else:
            attempts += 1
            print(f"Invalid credentials. {max_attempts - attempts} attempt(s) left.\n")

    except ValueError as ve:
        print(f"Error: {ve}\n")

    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")

if logged_in_user is None:
    print("\nAccess denied. Too many failed attempts!")

else:
    #Menu
    while True:
        try:
            print("MENU")
            print("1. View Profile")
            print("2. Change Password")
            print("3. Logout")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                print(f"\nUsername: {logged_in_user}")
                print("Status: Logged in successfully!\n")

            elif choice == "2":
                new_password = input("Enter new password: ")

                # Preventing empty passwords
                if new_password.strip() == "":
                    raise ValueError("Password cannot be empty.")

                users[logged_in_user] = new_password
                print("Password changed successfully!\n")

            elif choice == "3":
                print(f"\nGoodbye, {logged_in_user}!\n")
                break

            else:
                raise ValueError("Invalid menu choice. Please enter 1, 2, or 3.")

        except ValueError as ve:
            print(f"Input Error: {ve}\n")

        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Logging out safely...")
            break

        except Exception as e:
            print(f"Unexpected error: {e}\n")