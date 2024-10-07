import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def set_max_distances(start_vertex, graph, visited, max_distance_list):
    visited.add(start_vertex)
    first_max = second_max = 0 

    for child_info in graph[start_vertex]:
        end_vertex, distance = child_info
        if end_vertex in visited:
            continue
        
        temp_distance = distance + set_max_distances(end_vertex, graph, visited, max_distance_list)

        if temp_distance > first_max:
            first_max, second_max = temp_distance, first_max
        elif temp_distance > second_max:
            second_max = temp_distance
    
    max_distance_list[start_vertex] = (first_max, second_max)
    return first_max

def get_diameter(max_distance_list):
    answer = 0
    for first_max, second_max in max_distance_list.values():
        temp_answer = first_max + second_max
        answer = max(answer, temp_answer)
    return answer

v = int(input())
graph = defaultdict(list)
max_distance_list = {}

for _ in range(v):
    input_numbers = list(map(int, input().split()))
    start_vertex = input_numbers[0]

    for i in range(1, len(input_numbers), 2):
        end_vertex = input_numbers[i]
        if end_vertex == -1:
            break
        distance = input_numbers[i + 1]
        graph[start_vertex].append((end_vertex, distance))

visited = set() 
set_max_distances(1, graph, visited, max_distance_list)
print(get_diameter(max_distance_list))
