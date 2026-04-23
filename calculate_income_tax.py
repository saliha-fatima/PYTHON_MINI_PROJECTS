def calculate_income_tax(income):
    if income <= 10000:
        return 0
    elif income <= 20000:
        return (income - 10000) * 0.10
    else:
        return 1000 + (income - 20000) * 0.20

income_input = input("Enter your income: ")
income = float(income_input.replace('$', '').replace(',', ''))
if income < 0:
    print("Error: Income cannot be negative.")
else:
    tax = calculate_income_tax(income)
    print("Your income tax is: ${:.2f}".format(tax))