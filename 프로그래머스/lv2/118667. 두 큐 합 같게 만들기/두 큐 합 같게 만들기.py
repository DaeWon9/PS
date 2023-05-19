from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    
    max_count = (len(queue1) + len(queue2)) * 2
    
    if (queue1_sum + queue2_sum) % 2 == 1: # 홀수면 아예 불가능
        return -1
    
    while (queue1_sum != queue2_sum):
        if (answer > max_count):
            return -1
        
        if deque1 and queue1_sum > queue2_sum: #큰쪽에서 pop
            pop_value = deque1.popleft()
            deque2.append(pop_value)
            queue1_sum -= pop_value
            queue2_sum += pop_value
            answer += 1
            continue
            
        if deque2 and queue1_sum < queue2_sum: #큰쪽에서 pop
            pop_value = deque2.popleft()
            deque1.append(pop_value)
            queue2_sum -= pop_value
            queue1_sum += pop_value
            answer += 1
            continue
            
        answer += 1
    
    return answer