def print_downward_half_pyramid(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * i)

n = 5  # number of rows
print_downward_half_pyramid(n)