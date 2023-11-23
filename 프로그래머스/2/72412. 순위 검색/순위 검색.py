def b_search(arr, target_score):
    start = 0
    end = len(arr)
    mid = (start + end) // 2
    
    while start < end:
        mid = (start + end) //2
        if arr[mid] < target_score:
            start = mid + 1
        else:
            end = mid
            
    if arr[mid] < target_score: 
        return len(arr) - mid  -1
    else:
        return len(arr) - mid 


def solution(info, query):
    answer = []
    data = [[[[[] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]
    lang_dict = {"cpp" : 0, "java" : 1, "python" : 2}
    part_dict = {"backend" : 0, "frontend" : 1}
    career_dict = {"junior" : 0, "senior" : 1}
    food_dict = {"chicken" : 0, "pizza" : 1}
    
    for person_info in info:
        lang, part, career, food, score = person_info.split()
        lang_idx = lang_dict[lang]
        part_idx = part_dict[part]
        career_idx = career_dict[career]
        food_idx = food_dict[food]
        score = int(score)
        
        data[lang_idx][part_idx][career_idx][food_idx].append(score)
        

    for l in range(3):
        for p in range(2):
            for c in range(2):
                for f in range(2):
                    data[l][p][c][f].sort()

    
    for q in query:
        count = 0
        q = q.replace(" and ", " ")
        lang, part, career, food, score = q.split()
        score = int(score)
        
        if lang == "-":
            lang = [0,1,2]
        else:
            lang = [lang_dict[lang]]
            
        if part == "-":
            part = [0,1]
        else:
            part = [part_dict[part]]
            
        if career == "-":
            career = [0,1]
        else:
            career = [career_dict[career]]
            
        if food == "-":
            food = [0,1]
        else:
            food = [food_dict[food]]
            
        for l in lang:
            for p in part:
                for c in career:
                    for f in food:
                        if data[l][p][c][f]:
                            count += b_search(data[l][p][c][f], score)
        answer.append(count)
    return answer
