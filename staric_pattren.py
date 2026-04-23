n = 5  # Number of rows

for i in range(n):
    # Print spaces for pyramid alignment
    for j in range(n - i - 1):
        print(" ", end="")
    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")
    # Move to the next line after each row
    print()
