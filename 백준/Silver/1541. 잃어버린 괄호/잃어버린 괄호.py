import sys

input_string = sys.stdin.readline().rstrip()
splited_string = input_string.split("-")

int_list = []

for item in splited_string:
    sum = 0
    if "+" in item:
        for operand in item.split("+"):
            sum = sum + int(operand)
    else:
        sum = sum + int(item)
    
    int_list.append(sum)

result = int_list[0]

for item in int_list[1:]:
    result = result - item

print(result)