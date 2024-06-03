def is_palindrome(line):
    "checks the line for palindrome"
    length = len(line)
    for i in range(length // 2):
        if line[i] != line[length - i - 1]: #Compare letters from the beginning and from the end
            return False
    return True
line = "amaama"
if is_palindrome(line):
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")