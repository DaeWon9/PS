import sys

def is_palindrom(str):
    str_len = len(str)
    for i in range(str_len):
        if (str[i] != str[str_len - i - 1]):
            return False
    return True

input_string = sys.stdin.readline().rstrip()

max_palindrom_len = 0
for i in range(len(input_string)):
    if (is_palindrom(input_string[i:])):
        max_palindrom_len = max(len(input_string[i:]), max_palindrom_len)

if (max_palindrom_len == len(input_string)):
    print(len(input_string))
elif (max_palindrom_len == 1):
    print(len(input_string) * 2 - 1)
else:
    print((len(input_string) - max_palindrom_len) * 2 + max_palindrom_len)