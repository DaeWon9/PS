import sys

input_string = sys.stdin.readline().rstrip()

splited_string_1 = input_string.split('0')
splited_string_0 = input_string.split('1')

min_count = (len(splited_string_1) - splited_string_1.count(""), len(splited_string_0) - splited_string_0.count(""))
print(min(min_count))