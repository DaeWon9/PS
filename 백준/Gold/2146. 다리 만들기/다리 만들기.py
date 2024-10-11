import sys
from collections import deque, defaultdict
input = sys.stdin.readline

# UF
# loop
# 인접 육지끼리 그룹화 + 경계에 위치한 육지의 경우 queue에 추가하여 확장준비
# 확장
#########
# 그룹의 개수가 줄어드는 시점이 answer

def get_index(row, col):
    return row * N + col

def is_movable(dr, dc):
    return (0 <= dr < N and 0 <= dc < N)

def find(x):
    if (parent[x] == x):
        return x
    
    parent[x] = find(parent[x])

    group_children_dict[parent[x]].add(x)

    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if (x == y):
        return

    if (x < y): # 작은게 부모
        group_children_dict[x].add(y) # key: parent, value: children

        for child in group_children_dict[y]:
            parent[child] = x

        del group_children_dict[y]

        parent[y] = x
    else:
        group_children_dict[y].add(x)

        for child in group_children_dict[x]:
            parent[child] = y
        
        del group_children_dict[x]

        parent[x] = y

def union_ground():
    for row, col, group in queue:
        pivot_index = get_index(row, col)

        for i in range(4):
            dr = row + direction_y[i]
            dc = col + direction_x[i]
            target_index = get_index(dr, dc)

            if (is_movable(dr, dc) and target_index in visited_set): # ground
                if (find(pivot_index) != find(target_index)):
                    union(pivot_index, target_index)
                board[dr][dc] = 1

def spread_ground():
    global time
    spreaded_ground_dict = defaultdict(lambda: -1)
    
    for _ in range(len(queue)):
        row, col, group = queue.popleft()
        parent_group = find(group)

        for i in range(4):
            dr = row + direction_y[i]
            dc = col + direction_x[i]
            target_index = get_index(dr, dc)

            if (is_movable(dr, dc) and board[dr][dc] == 0):

                if (target_index not in visited_set): # new ground
                    queue.append((dr, dc, parent_group))
                    visited_set.add(target_index)
                    spreaded_ground_dict[target_index] = parent_group
                else:
                    if (board[dr][dc] == 0 and spreaded_ground_dict[target_index] != parent_group): # 다른그룹괴 동일 육지 확장
                        print((time + 1) * 2 - 1)
                        exit(0)

direction_x = [0, 0, 1, -1]
direction_y = [1, -1, 0, 0]

N = int(input())
board = []
queue = deque()
visited_set = set()

group_children_dict = defaultdict(set)

parent = [i for i in range(N * N)]
initial_group_count = 0
flag = False

for row in range(N):
    input_data = list(map(int, input().split()))

    for col, data in enumerate(input_data):
        if (data == 1):
            target_index = get_index(row, col)
            queue.append((row, col, target_index))
            visited_set.add(target_index)
            group_children_dict[target_index] = {target_index}

    board.append(input_data)

time = 0

while True:
    union_ground()

    group_count = len(group_children_dict)

    if (not flag):
        initial_group_count = group_count
        flag = True
    
    if (initial_group_count > group_count):
        print(time * 2)
        exit(0)

    spread_ground()

    time += 1