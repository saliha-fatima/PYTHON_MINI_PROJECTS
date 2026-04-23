def check_first_last(lst):
    if len(lst) < 1:
        return False
    return lst[0] == lst[-1]

print(check_first_last([1, 2, 3, 1]))   
print(check_first_last([1, 2, 3, 4]))   