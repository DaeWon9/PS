def solution(alp, cop, problems):    
    max_alp = 0
    max_cop = 0
    
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
        
    if(alp > max_alp):
        max_alp = alp
    if(cop > max_cop):
        max_cop = cop
    
    dp = [[999999999 for j in range(max_cop + 1)] for i in range(max_alp + 1)] # dp[알고력][코딩력] = time
    dp[alp][cop] = 0
        
    for current_alp in range(alp, max_alp + 1):
        for current_cop in range(cop, max_cop + 1):
            if current_alp < max_alp: # 그냥 순수 공부로 알고력 올리기 -> 시간 1 증가
                dp[current_alp + 1][current_cop] = min(dp[current_alp][current_cop] + 1, dp[current_alp + 1][current_cop])
            if current_cop < max_cop: # 그냥 순수 공부로 코딩력 올리기 -> 시간 1 증가
                dp[current_alp][current_cop + 1] = min(dp[current_alp][current_cop] + 1, dp[current_alp][current_cop + 1])

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems: # problems에 있는 문제 풀어서 올리기 -> 시간 cost만큼 증가
                if alp_req <= current_alp and cop_req <= current_cop: # 문제를 풀 수 있음
                    increased_alp = min(max_alp, current_alp + alp_rwd) # index error -> max_alp까지
                    increased_cop = min(max_cop, current_cop + cop_rwd)

                    dp[increased_alp][increased_cop] = min(dp[increased_alp][increased_cop], dp[current_alp][current_cop] + cost)
                    
    return dp[-1][-1] 