RT_score = [0, 0]
CF_score = [0, 0]
JM_score = [0, 0]
AN_score = [0, 0]

def cal_score(type, score):
    if (type == 'RT'):
        if (score < 4):
            RT_score[0] += 4 - score
        elif (score > 4):
            RT_score[1] += score - 4
    elif (type == 'TR'):
        if (score < 4):
            RT_score[1] += 4 - score
        elif (score > 4):
            RT_score[0] += score - 4

    elif (type == 'CF'):
        if (score < 4):
            CF_score[0] += 4 - score
        elif (score > 4):
            CF_score[1] += score - 4
    elif (type == 'FC'):
        if (score < 4):
            CF_score[1] += 4 - score
        elif (score > 4):
            CF_score[0] += score - 4
            
    elif (type == 'JM'):
        if (score < 4):
            JM_score[0] += 4 - score
        elif (score > 4):
            JM_score[1] += score - 4
    elif (type == 'MJ'):
        if (score < 4):
            JM_score[1] += 4 - score
        elif (score > 4):
            JM_score[0] += score - 4
            
    elif (type == 'AN'):
        if (score < 4):
            AN_score[0] += 4 - score
        elif (score > 4):
            AN_score[1] += score - 4
    elif (type == 'NA'):
        if (score < 4):
            AN_score[1] += 4 - score
        elif (score > 4):
            AN_score[0] += score - 4
    else: 
        pass

def getResult():
    result = ''
    if (RT_score[0] >= RT_score[1]):
        result += 'R'
    else:
        result += 'T'
        
    if (CF_score[0] >= CF_score[1]):
        result += 'C'
    else:
        result += 'F'
        
    if (JM_score[0] >= JM_score[1]):
        result += 'J'
    else:
        result += 'M'

    if (AN_score[0] >= AN_score[1]):
        result += 'A'
    else:
        result += 'N'
    
    return result
    
def solution(survey, choices):
    for type, score in zip(survey,choices):
        cal_score(type, score)
    
    answer = getResult()
    return answer