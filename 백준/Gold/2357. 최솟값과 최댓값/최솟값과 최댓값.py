import sys
input = sys.stdin.readline

def init_tree(node_idx, start, end):
    if (start == end):
        tree[node_idx] = (arr[start], arr[end])
        return tree[node_idx]
    
    mid = (start + end) // 2

    left = init_tree(node_idx * 2, start, mid)
    right = init_tree(node_idx * 2 + 1, mid + 1, end)

    tree[node_idx] = (min(left[0], right[0]), max(left[1], right[1]))

    return tree[node_idx]

def find_min_max(node_idx, start, end, target_start, target_end):
    if (end < target_start or target_end < start):
        return (1000000000, 0)
    
    mid = (start + end) // 2

    if (target_start <= start and end <= target_end):
        return tree[node_idx]
    else:
        left = find_min_max(node_idx * 2, start, mid, target_start, target_end)
        right = find_min_max(node_idx * 2 + 1, mid + 1, end, target_start, target_end)

        return (min(left[0], right[0]), max(left[1], right[1]))

N, M = map(int, input().split())
tree = [0 for _ in range(N * 4)]
arr = []

for _ in range(N):
    arr.append(int(input()))

init_tree(1, 0, N-1)

for _ in range(M):
    start, end = map(int, input().split())
    answer = find_min_max(1, 0, N-1, start - 1, end - 1)
    print(answer[0], answer[1])