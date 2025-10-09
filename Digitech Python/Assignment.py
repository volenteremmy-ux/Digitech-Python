# Access Control 
print("Welcome to Phoenix Access Control System\n")

username, password = "Phoenix", "Phoenix6789"
max_attempts, attempts = 3, 0
logged_in = False

while attempts < max_attempts:
    try:
        user = input("Enter username: ").strip()
        pwd = input("Enter password: ").strip()

        if not user or not pwd:
            raise ValueError("Username or password cannot be empty.")

        if user == username and pwd == password:
            print(f"\nAccess granted! Welcome, {user}!\n")
            logged_in = True
            break
        else:
            attempts += 1
            print(f"Invalid credentials. {max_attempts - attempts} attempt(s) left.\n")

    except ValueError as e:
        print(f"Error: {e}\n")

if not logged_in:
    print("Access denied. Too many failed attempts!")
#     exit()

# Menu 
while True:
    try:
        print("MENU")
        print("1. View Profile")
        print("2. Change Password")
        print("3. Logout")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print(f"\nUsername: {username}")
            print("Access Level: Owner")
            print("Status: Logged in successfully!\n")

        elif choice == "2":
            new_pass = input("Enter new password: ").strip()
            if not new_pass:
                raise ValueError("Password cannot be empty.")
            password = new_pass
            print("Password updated successfully!\n")

        elif choice == "3":
            print(f"\nGoodbye, {username}! Have a great day!\n")
            break

        else:
            raise ValueError("Invalid choice. Please enter 1, 2, or 3.\n")

    except ValueError as e:
        print(f"Error: {e}\n")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Logging out safely...")
        break