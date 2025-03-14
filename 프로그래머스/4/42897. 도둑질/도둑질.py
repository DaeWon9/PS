# 원형이 아니라 선형으로 보고
# case1: 첫 번째 집을 털었다고 가정 -> 마지막 집은 털지 못함
# case2: 첫 번째 집을 털지 않았다고 가정 -> 마지막 집을 터는것에 대한 유무 상관 x
# money가 0일때 추가 처리 필요

def solution(money):
    n = len(money)
    dp_1 = [0] * (n) # dp[i번째 집까지 털었을 때] = 돈의 최댓값
    dp_2 = [0] * (n)

    dp_1[0] = money[0] 
    dp_1[1] = money[0]
    # case1
    for i in range(2, n-1):
        dp_1[i] = max(dp_1[i-2] + money[i], dp_1[i-1])
    
    # case2
    dp_2[1] = money[1]
    for i in range(2, n):
        dp_2[i] = max(dp_2[i-2] + money[i], dp_2[i-1])
        
    return max(dp_1[n-2], dp_2[-1])
