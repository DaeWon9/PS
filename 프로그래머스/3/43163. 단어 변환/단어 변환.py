import heapq

def solution(begin, target, words):
    answer = 0
    word_len = len(begin)
    heap = [(0, begin)]
    visited = set([begin])
    
    while heap:
        count, cur_word = heapq.heappop(heap)
        
        if (cur_word == target):
            answer = count
            break
        
        for change_index in range(word_len):
            for word in words:
                if (word in visited):
                    continue
                    
                pivot_word = cur_word[:change_index] + cur_word[change_index + 1:]
                target_word = word[:change_index] + word[change_index + 1:]

                if (pivot_word == target_word):
                    heapq.heappush(heap, (count + 1, word))
                    visited.add(word)
    
    return answer