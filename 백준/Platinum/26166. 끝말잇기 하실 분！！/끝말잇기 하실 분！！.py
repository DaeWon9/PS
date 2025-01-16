import sys
from collections import defaultdict, deque
input = sys.stdin.readline

M = int(input())
words_list = []
rev_adj_vertices = defaultdict(list)
indegree = defaultdict(int)
end_char_status_dict = defaultdict(lambda: 'D')
queue = deque()

for _ in range(M):
    word = input().rstrip()
    words_list.append(word)
    s, e = word[0], word[-1]

    rev_adj_vertices[e].append(s) # e -> s
    indegree[e] = indegree[e]
    indegree[s] += 1

for key in indegree.keys():
    if (indegree[key] == 0): # leaf
        end_char_status_dict[key] = 'W' # key 로 끝나는 단어 선택 시 승리
        queue.append(key)

while queue:
    e = queue.popleft()

    for s in rev_adj_vertices[e]:
        if (end_char_status_dict[s] != 'D'): # 이미 결정
            continue

        if (end_char_status_dict[e] == 'W'):
            end_char_status_dict[s] = 'L'
            queue.append(s)
        else:
            indegree[s] -= 1
            if (indegree[s] == 0):
                end_char_status_dict[s] = 'W'
                queue.append(s)

answer = []
for word in words_list:
    e = word[-1]
    if (end_char_status_dict[e] == 'W'):
        answer.append(word)

print(len(answer))
answer.sort()
for ans in answer:
    print(ans)