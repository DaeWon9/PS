import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def print_children(prev_key_len, root):
    print(root[prev_key_len:])
    while adj_vertices[root]:
        adj_vertex = heapq.heappop(adj_vertices[root])
        print_children(len(root), root + adj_vertex)

N = int(input())
adj_vertices = defaultdict(list)
root_set = set()

for _ in range(N):
    input_data = list(map(str, input().rstrip().split()))
    data_len = int(input_data[0])
    root_set.add(input_data[1])
    key = input_data[1]

    for i in range(1, data_len):
        prev_data = '--' * (i-1) + input_data[i]
        next_data = '--' * (i) + input_data[i+1]
        if (next_data not in adj_vertices[key]):
            heapq.heappush(adj_vertices[key], next_data)
        key += next_data
        
for root in sorted(list(root_set)):
    print_children(0, root)