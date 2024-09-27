# Input and printing statements with corrections
print("Hello Amit world")  # Fixed 'print' typo

# Example for end parameter in print
print("Hello", end=" ")  # Removed undefined variable 'end'
print("Amit world")  # Added 'Amit' instead of 'Rajesh'

# Example with separator in print
print("Ram", "shyam", "Rohan", sep="#")  # Using '#' as a separator

# Taking input from the user and performing operations
x = int(input("Enter a number: "))  # Converting input to int
y = float(input("Enter CGPA: "))  # Converting input to float
print("Sum of x and y is:", x + y)

# Taking two inputs and performing operations
x, y = input("Enter two numbers: ").split()  # Using split to get two numbers
x = int(x)  # Converting input to int
y = int(y)  # Converting input to int
print("Sum of x and y is:", x + y)

# Logical operations and identity checks
x = 6
y = 7
print(x is y)  # False since x and y are different
y = x  # Now y refers to the same object as x
print(x is y)  # True since x and y refer to the same object

z = "7"
print(y is z)  # False, as y is an integer and z is a string

# List and membership checks
x = ["Rose", "Lotus"]
print("Rose" in x)  # True since "Rose" is in the list
print("rosi" in x)  # False since "rosi" is not in the list
print("Rose" not in x)  # False since "Rose" is in the list

# Comment examples
# This is a comment

# Simple if statement
x = 5
if x == 5:
    print("Hello Amit")  # Replaced Rajesh with Amit
