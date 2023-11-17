# 타겟 인덱스를 기준으로 맨해튼 거리가 2이하인 구역을 검사하고
# 해당 구역에 다른 P가 있다면 거리두기 유지 X
# but, 타겟 P와 2이하에 있는 P사이가 모두 파티션으로 막혀있으면 O

def isIndexValidate(row, col):
    if (row >= 0 and row < 5 and col >= 0 and col < 5):
        return True
    return False

def iskeepDistance(room, target_row, target_col): # room은 2차원배열
    
    #거리가 1일때 바로 false
    #상
    if (isIndexValidate(target_row - 1, target_col)):
        if (room[target_row - 1][target_col] == 'P'):
            return False
    #하
    if (isIndexValidate(target_row + 1, target_col)):
        if (room[target_row + 1][target_col] == 'P'):
            return False
    #좌
    if (isIndexValidate(target_row, target_col - 1)):
        if (room[target_row][target_col - 1] == 'P'):
            return False
    #우
    if (isIndexValidate(target_row, target_col + 1)):
        if (room[target_row][target_col + 1] == 'P'):
            return False
    
    
    
    # 상상
    if (isIndexValidate(target_row, target_col + 2)):
        if (room[target_row][target_col + 2] == 'P'):
            if (room[target_row][target_col + 1] == 'O'):
                return False
    
    # 좌좌
    if (isIndexValidate(target_row, target_col - 2)):
        if (room[target_row][target_col - 2] == 'P'):
            if(room[target_row][target_col - 1] == 'O'):
                return False
    # 우우
    if (isIndexValidate(target_row, target_col + 2)):
        if (room[target_row][target_col + 2] == 'P'):
            if(room[target_row][target_col + 1] == 'O'):
                return False
            
    # 하하
    if (isIndexValidate(target_row + 2, target_col)):
        if (room[target_row + 2][target_col] == 'P'):
            if(room[target_row + 1][target_col] == 'O'):
                return False
            
    # 좌상
    if (isIndexValidate(target_row - 1, target_col - 1)):
        if (room[target_row - 1][target_col - 1] == 'P'):
            if (room[target_row - 1][target_col] == 'O' or room[target_row][target_col - 1] == 'O'):
                return False
    # 좌하
    if (isIndexValidate(target_row + 1, target_col - 1)):
        if (room[target_row + 1][target_col - 1] == 'P'):
            if (room[target_row][target_col - 1] == 'O' or room[target_row + 1][target_col] == 'O'):
                return False
    # 우상
    if (isIndexValidate(target_row - 1, target_col + 1)):
        if (room[target_row - 1][target_col + 1] == 'P'):
            if (room[target_row - 1][target_col] == 'O' or room[target_row][target_col + 1] == 'O'):
                return False
    # 우하
    if (isIndexValidate(target_row + 1, target_col + 1)):
        if (room[target_row + 1][target_col + 1] == 'P'):
            if (room[target_row][target_col + 1] == 'O' or room[target_row + 1][target_col] == 'O'):
                return False

    
    return True

def solution(places): # P : 응시자가 앉아있는 자리 / 0 : 빈 테이블 / X : 파티션
    
    answer = []
    
    for room in places:
        isKeep = True
        for row in range(5):
            if (not isKeep):
                break
            for col in range(5):
                if (room[row][col] == 'P'):
                    isKeep = iskeepDistance(room, row, col)
                
                    if (not isKeep):
                        break
                
        if (isKeep):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer