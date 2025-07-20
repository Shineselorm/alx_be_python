# Prompt the user to enter a positive integer for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to print each row
while row < size:
    # Use a for loop to print the asterisks in a row
    for col in range(size):
        print("*", end="")
    # Print a newline after each row
    print()
    row += 1
