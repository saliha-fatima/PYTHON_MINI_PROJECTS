def count_substring(string, substring):
    return string.count(substring)

string = "Emma is a good girl, Emma is a nice girl, Emma is a smart girl"
substring = "Emma"
count = count_substring(string, substring)
print(f"The substring '{substring}' appears {count} times in the string.")