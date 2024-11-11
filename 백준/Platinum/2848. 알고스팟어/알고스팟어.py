import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
word_list = []
all_set = set()
adj_vertices = defaultdict(set)
indegree_vertices = defaultdict(set)
indegree = defaultdict(int)
queue = deque() 
answer = []

for _ in range(N):
    word_list.append(input().rstrip())

for word in word_list:
    for ch in word:
        all_set.add(ch)

possbile_flag = True        

for i in range(N-1):
    cur_word, next_word = word_list[i], word_list[i+1]
    cur_word_len, next_word_len = len(cur_word), len(next_word)

    min_len = cur_word_len
    is_short = True

    if (min_len > next_word_len):
        min_len = next_word_len
        is_short = False

    for j in range(1, min_len + 1):
        if (cur_word[:j] == next_word[:j]):
            if (j == min_len and not is_short):
                possbile_flag = False
            continue

        v1, v2 = cur_word[j-1], next_word[j-1] 
        adj_vertices[v1].add(v2)
        indegree_vertices[v2].add(v1)
        break
    
if (not possbile_flag):
    print("!")
    exit(0)

for key in all_set:
    indegree[key] = len(indegree_vertices[key])

for key in indegree.keys():
    if (indegree[key] == 0):
        queue.append(key)
        answer.append(key)

flag = False
all_count = len(all_set)

for _ in range(all_count):
    if (len(queue) > 1):
        flag = True
    
    if (not queue):
        print("!")
        exit(0)

    v = queue.popleft()

    for adj_vertex in adj_vertices[v]:
        indegree[adj_vertex] -= 1
        
        if (indegree[adj_vertex] == 0):
            queue.append(adj_vertex)
            answer.append(adj_vertex)

if (flag):
    print("?")
else:
    print(''.join(answer))