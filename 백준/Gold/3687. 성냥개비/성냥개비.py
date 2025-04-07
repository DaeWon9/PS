import sys
from collections import deque
input = sys.stdin.readline

count_info_dict = {
    2: ['1'],
    3: ['7'],
    4: ['4'],
    5: ['2'],
    6: ['0', '6'],
    7: ['8']
}

def get_min_value(n):
    dp = [-1] * (n + 1)
    queue = deque()
    queue.append((0, ""))

    while queue:
        count, path = queue.popleft()
        if (count > n):
            continue

        for digit_count, digits in count_info_dict.items():
            for digit in digits:
                if (path == "" and digit == '0'):
                    continue

                new_count = count + digit_count
                new_value = path + digit

                if (new_count > n):
                    continue

                if (dp[new_count] == -1 or dp[new_count] > int(new_value)):
                    queue.append((new_count, new_value))
                    dp[new_count] = int(new_value)
    
    return dp[-1]

T = int(input())

for _ in range(T):
    n = int(input())
    max_v = ''
    
    if (n % 2 == 0): # 짝    
        max_v = '1' * (n // 2)
    else:
        max_v = '7' + '1' * (n // 2 - 1)

    print(get_min_value(n), max_v)