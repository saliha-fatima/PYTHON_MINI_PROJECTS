def factorial(n):
    """Calculate the factorial of a number"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sort_factorial_order(lst):
    """Sort a list in factorial order"""
    # Calculate the factorial of each number in the list
    factorial_list = [(num, factorial(num)) for num in lst]
    
    # Sort the list based on the factorials
    sorted_list = sorted(factorial_list, key=lambda x: x[1])
    
    # Return the sorted list of numbers
    return [num for num, _ in sorted_list]

# Example usage:
numbers = [3, 1, 2, 4]
print("Original List:", numbers)
print("Sorted List in Factorial Order:", sort_factorial_order(numbers))