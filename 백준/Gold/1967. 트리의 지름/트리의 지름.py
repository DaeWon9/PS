import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def calc_max_sum(root_id):
    if(len(sum_dict[root_id]) == 0):
        if (len(graph_dict[root_id]) == 0):
            return 0
        
        sum_list = []

        for child_id, value in graph_dict[root_id]:
            sum = value
            sum += calc_max_sum(child_id)
            sum_list.append(sum)

        sum_list.sort(reverse = True)
        sum_dict[root_id] = sum_list
    
    return max(sum_dict[root_id])

graph_dict = defaultdict(list)
sum_dict = defaultdict(list)
parent_id_list = []
answer = 0

n = int(input())

for _ in range(n-1):
    v1, v2, value = map(int, input().split())
    graph_dict[v1].append((v2, value))
    parent_id_list.append(v1)

for root_id in parent_id_list:
    calc_max_sum(root_id)

for result_item in sum_dict.items():
    if (len(result_item[1]) == 0):
        continue

    temp_answer = 0
    if (len(result_item[1]) == 1):
        temp_answer = result_item[1][0]
    else:
        temp_answer = result_item[1][0] + result_item[1][1]

    if (answer < temp_answer):
        answer = temp_answer

print(answer)