import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
R = int(input())
adj_vertices = [[] for _ in range(N)]
root = 0
for i in range(N):
    P = A[i]
    if (P == -1):
        root = i
        continue

    adj_vertices[P].append(i)


if (R == root):
    print(0)
    exit(0)


queue = deque()
queue.append(root) # root
answer = 0

while queue:
    v = queue.popleft()
    
    flag = (R in adj_vertices[v])

    if (len(adj_vertices[v]) == 0 or (flag and len(adj_vertices[v]) == 1)):
        answer += 1
        continue
    
    for adj_vertex in adj_vertices[v]:
        if (adj_vertex == R):
            continue
        
        queue.append(adj_vertex)

print(answer)
