import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solve(v):
    visited.add(v)
    for adj_vertex in adj_vertices[v]:
        if (adj_vertex in visited):
            continue

        solve(adj_vertex)
        # 내가 얼리 아답터가 아니면 자식은 얼리 아답터
        early_adapter_count[0][v] += early_adapter_count[1][adj_vertex]
        # 내가 얼리 아답터면 자식은 아무거나
        early_adapter_count[1][v] += min(early_adapter_count[0][adj_vertex], early_adapter_count[1][adj_vertex])
    

N = int(input())
adj_vertices = defaultdict(list)
visited = set()
root = 1 # 1번 노드를 root로 가정
early_adapter_count = [[i for _ in range(N+1)] for i in range(2)]

for _ in range(N-1):
    a, b = map(int, input().split())
    adj_vertices[a].append(b)
    adj_vertices[b].append(a)

solve(root)
print(min(early_adapter_count[0][root], early_adapter_count[1][root]))
