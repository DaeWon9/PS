N = int(input())

case_count_dict = dict()
case_count_dict[1] = 1
case_count_dict[2] = 2
case_count_dict[3] = 4
case_count_dict[4] = 7
case_count_dict[5] = 13

for _ in range(N):
    input_value = int(input())
    if (input_value < 6):
        print(case_count_dict[input_value])
    else:
        for i in range(6, input_value+1):
            case_count_dict[i] = case_count_dict[i-3] + case_count_dict[i-2] + case_count_dict[i-1]
        print(case_count_dict[input_value])