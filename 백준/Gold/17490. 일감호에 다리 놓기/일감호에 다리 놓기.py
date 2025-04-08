import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
S = [0] + list(map(int, input().split()))
disconnected_infos = set()
min_stone_count = [1000000] * (N+2)

for _ in range(M):
    u, v = map(int, input().split())

    if (u > v):
        u, v = v, u

    disconnected_infos.add((u, v))

is_last_connected = True
if ((1, N) in disconnected_infos):
    is_last_connected = False
    disconnected_infos.remove((1, N))

min_stone_count[1] = S[1]
group_id = 1
for i in range(1, N):
    if ((i, i+1) in disconnected_infos):
        group_id += 1
    
        min_stone_count[group_id] = min(min_stone_count[group_id], S[i+1])
    else:
        min_stone_count[group_id] = min(min_stone_count[group_id], S[i], S[i+1])

stone_sum = 0

if (is_last_connected):
    stone_sum = sum(min_stone_count[2:group_id]) + min(min_stone_count[1], min_stone_count[group_id])
else:
    stone_sum = sum(min_stone_count[1:group_id+1])

if (group_id == 1 or M <= 1):
    print("YES")
elif (stone_sum <= K):
    print("YES")
else:
    print("NO")
