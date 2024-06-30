import sys
from collections import defaultdict
input = sys.stdin.readline

def setDict(dict, target):
    for i in range(len(target)):
        if (target[i].isdigit()):
            continue
        
        if (i == len(target) - 1):
            dict[target[i]] += 1
            break

        if (target[i + 1].isdigit()):
            dict[target[i]] += int(target[i + 1])
        else:
            dict[target[i]] += 1


input_data = input().rstrip()
input_data = input_data.split('=')
right = input_data[1]
left, mid = input_data[0].split('+')

left_dict = defaultdict(int)
mid_dict = defaultdict(int)
right_dict = defaultdict(int)

setDict(left_dict, left)
setDict(mid_dict, mid)
setDict(right_dict, right)

for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            status = [False, False, False]
            for idx, key in enumerate(['C', 'H', 'O']):
                if(int(left_dict[key]) * i + int(mid_dict[key]) * j == int(right_dict[key]) * k):
                    status[idx] = True
            
            if(status.count(True) == 3):
                print(i, j, k)
                exit(0)