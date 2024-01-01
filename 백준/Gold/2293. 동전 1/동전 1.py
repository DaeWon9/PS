import sys

coin_count, target_value = map(int, sys.stdin.readline().split())

coin_list = []

for _ in range (coin_count):
    coin_list.append(int(sys.stdin.readline()))

dp = [0 for _ in range(target_value + 1)]
dp[0] = 1

for coin in coin_list: # coin_list[ 1, 2, 5 ]
    for dp_index in range(coin, target_value + 1):
        dp[dp_index] = dp[dp_index] + dp[dp_index - coin]

print(dp[target_value])