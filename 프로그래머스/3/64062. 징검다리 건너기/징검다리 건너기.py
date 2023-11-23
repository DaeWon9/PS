from collections import deque

def solution(stones, k):   
    result = list()
    dq = deque()
    
    if (len(stones) == k):
        return max(stones)
    
    for i in range(len(stones)):
        while dq and dq[-1][1] < stones[i]:
            dq.pop()

        dq.append((i, stones[i]))

        while dq and dq[0][0] < i - k + 1:
            dq.popleft()

        result.append(dq[0][1])

    return min(result[k-1:])