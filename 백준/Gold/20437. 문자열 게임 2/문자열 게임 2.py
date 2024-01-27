import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def solution(input_string, k):
    min_len = 10001
    max_len = 0

    alphabet_dict = defaultdict(list)

    for i in range(len(input_string)):
        ch = input_string[i]
        alphabet_dict[ch].append(i)
    
    result_list = list(alphabet_dict.items())
    result_list.sort(key = lambda x : -len(x[1]))

    for alphabet, index_list in result_list:
        index_list_len = len(index_list)
        if (index_list_len < k):
            break
        
        queue = deque()
        for i in range(index_list_len):            
            queue.append(index_list[i])
            if (len(queue) == k):
                temp_len = queue[-1] - queue[0] + 1
                if (min_len > temp_len):
                    min_len = temp_len
                if (max_len < temp_len):
                    max_len = temp_len
                queue.popleft()

    if (max_len == 0):
        print(-1)
    else:
        print(min_len, max_len)

t = int(input())

for _ in range(t):
    input_string = input().rstrip()
    k = int(input())
    solution(input_string, k)