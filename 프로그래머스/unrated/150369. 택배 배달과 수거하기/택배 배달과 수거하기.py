def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver = 0
    pickup = 0

    for i in range(n-1, -1, -1):

        cnt = 0

        deliver -= deliveries[i] # 배열의 끝 부터 수행해야 할 값 -
        pickup -= pickups[i]

        while (deliver < 0 or pickup < 0): # 양수가 될 때 까지 최대 수용량만큼 더해주면서 카운트 증가
            deliver += cap
            pickup += cap
            cnt += 1

        answer += (i + 1) * 2 * cnt # 거리 * 2 * 카운트 

    return answer