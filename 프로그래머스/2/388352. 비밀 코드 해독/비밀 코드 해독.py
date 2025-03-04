def combinations(arr, n, start = 0, path = [], result = []):
    if (len(path) == n):
        result.append(path[:])
        return
    
    for i in range(start, len(arr)):
        path.append(arr[i])
        combinations(arr, n, i+1, path, result)
        path.pop()
        
    return result

def solution(n, q, ans):
    answer = 0
    all_set = set(range(1, n+1))
    arr = sorted(zip(ans, q))
    
    for ans, q in arr:
        if (ans > 0):
            break
        
        for data in q:
            try:
                all_set.remove(data)
            except:
                pass

    for combi in combinations(list(all_set), 5):
        pivot_set = set(combi)
        flag = True
        for ans, q in arr:
            intersection_set = pivot_set.intersection(set(q))
            if (len(intersection_set) != ans):
                flag = False
                break
                
        if (flag):
            answer += 1

    return answer