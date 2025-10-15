try:
    number = float(input("Enter a number: "))  
    result = 100 / number                      
    print(f"Result: {result}")
except ZeroDivisionError:
    print("You can't divide by zero!")          
except ValueError:
    print("Invalid input. Please enter a number.")  