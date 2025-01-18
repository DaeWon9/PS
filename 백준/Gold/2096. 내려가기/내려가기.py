import sys
input = sys.stdin.readline

N = int(input())

prev_min_dp = [0] * 3
prev_max_dp = [0] * 3
cur_min_dp = [0] * 3
cur_max_dp = [0] * 3

first_row = list(map(int, input().split()))
prev_min_dp[:] = first_row
prev_max_dp[:] = first_row

for _ in range(1, N):
    row = list(map(int, input().split()))
    for col in range(3):
        if (col == 0):
            cur_max_dp[col] = max(row[col] + prev_max_dp[col],
                                  row[col] + prev_max_dp[col + 1])
            cur_min_dp[col] = min(row[col] + prev_min_dp[col],
                                  row[col] + prev_min_dp[col + 1])
        elif (col == 2):
            cur_max_dp[col] = max(row[col] + prev_max_dp[col],
                                  row[col] + prev_max_dp[col - 1])
            cur_min_dp[col] = min(row[col] + prev_min_dp[col],
                                  row[col] + prev_min_dp[col - 1])
        else:
            cur_max_dp[col] = max(row[col] + prev_max_dp[col],
                                  row[col] + prev_max_dp[col - 1],
                                  row[col] + prev_max_dp[col + 1])
            cur_min_dp[col] = min(row[col] + prev_min_dp[col],
                                  row[col] + prev_min_dp[col - 1],
                                  row[col] + prev_min_dp[col + 1])
    
    prev_min_dp, cur_min_dp = cur_min_dp, prev_min_dp
    prev_max_dp, cur_max_dp = cur_max_dp, prev_max_dp

print(max(prev_max_dp), min(prev_min_dp))
