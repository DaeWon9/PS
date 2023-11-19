def solution(s):
    answer = []
    
    s = s.replace("{{", "").replace("}}","")
    datas = s.split("},{")
       
    datas.sort(key=lambda x : len(x))
    for data in datas:
        data_list = list(map(int, data.split(",")))
        
        add_datas = list(set(data_list) - set(answer))
        
        for add_data in add_datas:
            answer.append(add_data)
    
    



    return answer