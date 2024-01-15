import sys
import heapq

n = int(sys.stdin.readline())
time_list = []
for _ in range(n):
    time_list.append(list(map(int, sys.stdin.readline().split())))

time_list.sort() # 시작순서로 sort
room = []
heapq.heappush(room, time_list[0][1]) # 종료시간 push

for i in range(1, n):
    if time_list[i][0] < room[0]:
        heapq.heappush(room, time_list[i][1]) 
    else: 
        heapq.heappop(room)
        heapq.heappush(room, time_list[i][1])

print(len(room))