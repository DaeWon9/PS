import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_value_set = set()
dp = [2147483647 for _ in range(k+1)]
dp[0] = 0

for _ in range(n):
    input_value = int(input())
    if (k < input_value):
        continue

    coin_value_set.add(input_value)

for goal in range(1, k+1):
    for coin_value in coin_value_set:
        if (goal < coin_value):
            continue
        # 원래 값 vs coin_value 가 더해지는 경우
        dp[goal] = min(dp[goal], dp[goal-coin_value]+1)

if (dp[k] == 2147483647):
    print(-1)
else:
    print(dp[k])