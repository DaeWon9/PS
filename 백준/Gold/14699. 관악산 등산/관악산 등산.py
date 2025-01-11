import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = map(int, input().split())
input_heights = list(map(int, input().split()))
height_list = [(input_heights[i], i+1) for i in range(N)]

height_dict = defaultdict(int)
adj_vertices = defaultdict(list)
queue = deque()
dp = [1] * (N)

for height, id in height_list:
    height_dict[id] = height
    queue.append((id, 1))

for _ in range(M):
    v1, v2 = map(int, input().split())

    v1_height = height_dict[v1]
    v2_height = height_dict[v2]

    if (v1_height < v2_height):
        adj_vertices[v2].append(v1)
    elif (v1_height > v2_height):
        adj_vertices[v1].append(v2)

while queue:
    v, c = queue.popleft()

    if (dp[v-1] > c):
        continue

    for adj_vertex in adj_vertices[v]:
        if (dp[adj_vertex-1] < c+1):
            dp[adj_vertex-1] = c+1

            queue.appendleft((adj_vertex, c+1))

for ans in dp:
    print(ans)