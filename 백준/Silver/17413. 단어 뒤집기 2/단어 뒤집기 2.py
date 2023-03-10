import sys

input_string = sys.stdin.readline().rstrip()

result_string = ""
is_tag = False

is_start_none_tag = False
start_index = 0
end_index = 0
for i in range(len(input_string)):
    if (input_string[i] == "<"):
        is_tag = True
    elif (input_string[i - 1] == ">"):
        is_tag = False

    if(is_tag):
        if (is_start_none_tag):
            end_index = i
            is_start_none_tag = False

            for j in range(end_index - 1, start_index - 1, -1):
                result_string = result_string + input_string[j]
        result_string = result_string + input_string[i]

    else: #태그 인덱스가 아니면
        if (not is_start_none_tag):
            is_start_none_tag = True
            start_index = i

        if (is_start_none_tag and input_string[i] == " "):
            end_index = i - 1
            for j in range(end_index, start_index - 1, -1):
                result_string = result_string + input_string[j]
            result_string = result_string + " "
            start_index = i + 1

        if (is_start_none_tag and i == len(input_string) -1):
            end_index = i
            for j in range(end_index, start_index - 1, -1):
                result_string = result_string + input_string[j]
        
print(result_string)