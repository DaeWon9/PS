import itertools

N = int(input())
dice_number = list(map(int, input().split(" "))) # A,B,C,D,E,F 순으로 입력, 정반대편쌍 (A,F), (B,E), (C,D) -> 노출될 수 없음.
sorted_dice_number = sorted(dice_number)

dice_dict = {
    'A' : dice_number[0],
    'B' : dice_number[1],
    'C' : dice_number[2],
    'D' : dice_number[3],
    'E' : dice_number[4],
    'F' : dice_number[5],
}

dice_dict_keys = list(dice_dict.keys())

two_combination = list(itertools.combinations(dice_dict_keys, 2))
two_combination.remove(('A','F'))
two_combination.remove(('B','E'))
two_combination.remove(('C','D'))

two_showed_number_sum_list = []
for key in two_combination:
    two_showed_number_sum_list.append(dice_dict[key[0]] + dice_dict[key[1]])

three_combination = list(itertools.combinations(dice_dict_keys, 3))

three_showed_number_sum_list = []
for key in three_combination:
    if ('A' in key and 'F' in key):
        pass
    elif ('B' in key and 'E' in key):
        pass
    elif ('C' in key and 'D' in key):
        pass
    else:
        three_showed_number_sum_list.append(dice_dict[key[0]] + dice_dict[key[1]] + dice_dict[key[2]])
        

one_showed_number_sum = min(dice_number)

two_showed_number_sum = min(two_showed_number_sum_list)

three_showed_number_sum = min(three_showed_number_sum_list)

result = (three_showed_number_sum * 4) + (two_showed_number_sum * ((N-2) * 8 + 4)) + (one_showed_number_sum * ((N-2)**2 * 5 + (N-2) * 4))

if (N == 1):
    print(sum(sorted_dice_number) - max(sorted_dice_number))
else:
    print(result)