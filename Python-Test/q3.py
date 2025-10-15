password = "python123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Enter your password: ")

    if password == password:
        print("Access granted.")
        break
    else:
        attempts += 1
        print(f"Incorrect password. {max_attempts - attempts} attempt(s) left.")

if attempts == max_attempts:
    print("Access denied. Try again later.")
