import sys
input = sys.stdin.readline

def init_tree(node_idx, start, end):
    if (start == end):
        tree[node_idx] = (A[start], start)
        return tree[node_idx]

    mid = (start + end) // 2
    left = init_tree(node_idx * 2, start, mid)
    right = init_tree(node_idx * 2 + 1, mid + 1, end)

    tree[node_idx] = min(left, right)
    return tree[node_idx]

def find_min(node_idx, start, end, rs, re):
    if (re < start or rs > end):
        return (2147483647, -1)
    
    if (rs <= start and end <= re):
        return tree[node_idx]

    mid = (start + end) // 2
    left = find_min(node_idx * 2, start, mid, rs, re)
    right = find_min(node_idx * 2 + 1, mid + 1, end, rs, re)

    return min(left, right)

def update(node_idx, start, end, ti, tv):
    if (ti < start or end < ti):
        return
    
    if (start == end):
        tree[node_idx] = (tv, ti)
        return
    
    mid = (start + end) // 2
    update(node_idx * 2, start, mid, ti, tv)
    update(node_idx * 2 + 1, mid + 1, end, ti, tv)
    tree[node_idx] = min(tree[node_idx * 2], tree[node_idx * 2 + 1])

N = int(input())
A = list(map(int, input().split()))
M = int(input())
tree = [(0, 0) for _ in range(N * 4)]

init_tree(1, 0, N-1)

for _ in range(M):
    a, b, c = map(int, input().split())

    if (a == 1):
        update(1, 0, N-1, b-1, c)
    else:
        result = find_min(1, 0, N-1, b-1, c-1)
        print(result[1] + 1)
