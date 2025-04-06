import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def solve(v):
    global cnt

    l, r = child_list[v] 
    visited_vertex_set.add(v)

    cnt += 1

    if (l != -1 and l not in visited_vertex_set):
        parent_stack.append(v)
        solve(l)
    
    if (r != -1 and r not in visited_vertex_set):
        parent_stack.append(v)
        solve(r)

    if (len(visited_vertex_set) == N and v == finish_node):
        print(cnt-1)
        exit(0)

    if (parent_stack):
        solve(parent_stack.pop())


N = int(input())
child_list = defaultdict(tuple)
visited_vertex_set = set()
parent_stack = []
cnt = 0

finish_node = 0

for _ in range(N):
    v, l, r = map(int, input().split())
    child_list[v] = (l, r)
    
    if (v == 1):
        if (r == -1):
            finish_node = 1

if (finish_node == 0): # find finish_node
    target_node = 1

    while True:
        target_node = child_list[target_node][1]

        if (target_node == -1):
            break

        finish_node = target_node

solve(1)