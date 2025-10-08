# #We are performing the for loop in our program
# for number in range(1,10):
#     print(number)
# # Triangular check
# for number in range(1,10):
#     print(number * "*")
# #Checking even numbers
# for number in range(1,10):
#     if number %2 == 0:
#         print(number )

# #checking odd numbers
# for number in range(1,10):
#     if number %2 == 1:
#         print(number )

#We are creating the "while loop" for our program
trial = 3
attempt = 0

while attempt < trial:
    value = input("Enter the password")
    if value == "Phoenix6789":
        print("Log in successful!")
        break
    else:
        print("Password is wrong, try again!!")
        attempt +=1

else:
    print("You failed, number of attempts are over!!")