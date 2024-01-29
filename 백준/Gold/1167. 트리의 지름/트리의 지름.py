import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def set_max_distances(start_vertex):
    if (max_distance_list[start_vertex]):
        return max(max_distance_list[start_vertex])
    
    visted[start_vertex] = True
    temp_list = []

    for child_info in graph[start_vertex]:
        if (visted[child_info[0]]):
            continue

        temp_distacne = child_info[1]
        temp_distacne += set_max_distances(child_info[0])
    
        temp_list.append(temp_distacne)
    
    temp_list.sort(reverse = True)
    max_distance_list[start_vertex] = temp_list

    if (max_distance_list[start_vertex]):
        return max(max_distance_list[start_vertex])
    return 0

def get_diameter():
    answer = 0
    max_distance_list.sort(key = lambda x : -len(x))

    for item in max_distance_list:
        temp_answer = 0
        if (not item):
            break
        if (len(item) > 1):
            temp_answer = item[0] + item[1]
        else:
            temp_answer = item[0]

        if (answer < temp_answer):
            answer = temp_answer

    return answer

v = int(input())
graph = defaultdict(list)
max_distance_list = [[]] * (v + 1)
visted = [False] * (v + 1)
visted[1] = True

for _ in range(v):
    input_numbers = list(map(int, input().split()))
    start_vertex = input_numbers[0]

    for i in range(1, len(input_numbers), 2):
        end_vertex = input_numbers[i]

        if (end_vertex == -1):
            break
        
        distance = input_numbers[i+1]
        graph[start_vertex].append((end_vertex, distance))

set_max_distances(1)
print(get_diameter())