#dp[i][j] = i번째 물건까지 훔치고, B의 흔적이 j일때, A의 최소흔적
def solution(info, n, m):
    info_len = len(info)
    INF = 2147483647

    dp = [[INF for i in range(m)] for _ in range(info_len+1)]
    dp[0][0] = 0
    
    for i in range(info_len):
        a, b = info[i]
        dp_idx = i+1
        
        for bb in range(m-1, -1, -1):
            if (bb < b):
                dp[dp_idx][bb] = dp[dp_idx-1][bb] + a # a가 훔치는 경우
                continue
                
            dp[dp_idx][bb] = min(
                dp[dp_idx-1][bb] + a, # a가 훔치는 경우
                dp[dp_idx-1][bb-b], # b가 훔치는 경우
            )

                
    answer = min(dp[-1])

    return answer if answer < n else -1  # 불가능하면 -1 반환
