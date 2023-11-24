# 최대 2억명 -> 이분탐색?
# mid 명이 건널 수 있다고 가정
    
def solution(stones, k):   
    answer = 1
    start = 1
    end = max(stones)

    while(start <= end):
        is_possible = True
        mid  = (start + end) // 2

        cnt = 0
        for stone in stones:
            if (stone - mid < 0):
                cnt += 1
                if (cnt >= k): # 건너기 불가능
                    is_possible = False
                    break
            else:
                cnt = 0
        
        if (is_possible):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer
