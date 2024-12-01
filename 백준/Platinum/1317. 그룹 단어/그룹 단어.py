import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
indegree = defaultdict(int)
adj_vertices = defaultdict(list)
char_count = defaultdict(int)
queue = deque()
word_set = set()
possible_flag = True

group_word_list = [''] * 50
group_id = 0

def is_group_word():
    target_word = ''.join(group_word_list[:group_id])
    for word in word_set:
        if (word not in target_word):
            return [False, target_word]

    return [True, target_word]
    
for _ in range(N):
    input_word = input().rstrip()
    diff_flag = False

    for i in range(len(input_word)-1):
        prev, next = input_word[i], input_word[i+1]
        char_count[prev] += 1

        if (prev == next): 
            continue
        else:
            diff_flag = True

        indegree[next] += 1
        adj_vertices[prev].append(next)

    if (diff_flag):
        if (input_word in word_set):
            possible_flag = False

    word_set.add(input_word)
    char_count[input_word[-1]] += 1

if (not possible_flag):
    print('gg')
    exit(0)

for key in char_count.keys():
    if (indegree[key] == 0):
        queue.append((group_id, key))
        group_word_list[group_id] += key * char_count[key]
        group_id += 1

flag = False
all_count = len(char_count.keys())

for _ in range(all_count):
    if (len(queue) > 1):
        flag = True

    if (not queue):
        print('gg')
        exit(0)

    id, v = queue.popleft()

    for adj_vertex in adj_vertices[v]:
        indegree[adj_vertex] -= 1

        if (indegree[adj_vertex] == 0):
            queue.append((id, adj_vertex))
            group_word_list[id] += adj_vertex * char_count[adj_vertex]

is_possible, answer = is_group_word()
if (not is_possible):
    print('gg')
    exit(0)

if (flag):
    print('-_-')
else:
    print(answer)
