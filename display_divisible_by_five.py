def display_divisible_by_five(lst):
    if not lst:
        print("The list is empty.")
        return
    for num in lst:
        if not isinstance(num, (int, float)):
            print(f"Skipping non-numeric value: {num}")
            continue
        if num % 5 == 0:
            print(num)

 
numbers = [10, 20, 33, 45, 50, 67, 75, 88, 95]
display_divisible_by_five(numbers)