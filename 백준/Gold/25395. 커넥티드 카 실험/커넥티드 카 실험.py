from collections import deque
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
locations = list(map(int, input().split()))
fuels = list(map(int, input().split()))

cars = [(i + 1, locations[i], fuels[i]) for i in range(N)] # index, location, fuel

queue = deque()
visited = [False] * (N + 1)

queue.append(cars[S - 1])
visited[S] = True

while queue:
    cur_idx, cur_loc, cur_fuel = queue.popleft()
    
    for i in range(cur_idx - 2, -1, -1):
        if (cars[i][1] < cur_loc - cur_fuel):
            break
        if (visited[cars[i][0]]):
            continue
        
        queue.append(cars[i])
        visited[cars[i][0]] = True

    for i in range(cur_idx - 1, N):
        if (cars[i][1] > cur_loc + cur_fuel):
            break
        if (visited[cars[i][0]]):
            continue
        
        queue.append(cars[i])
        visited[cars[i][0]] = True

result = [str(i) for i in range(1, N + 1) if visited[i]]
print(" ".join(result))
