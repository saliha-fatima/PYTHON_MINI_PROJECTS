# Initialize an empty list to store the factorials
factorials = []

# Loop through numbers from 1 to 10
for i in range(1, 11):
    # Calculate the factorial of the current number
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    
    # Append the result to the list
    factorials.append((i, factorial))

# Print the table
print("Factorial Table:")
print("---------------")
for num, fact in factorials:
    print(f"{num}! = {fact}")