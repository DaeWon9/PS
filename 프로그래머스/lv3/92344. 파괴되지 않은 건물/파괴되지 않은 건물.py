def solution(board, skills):
    answer = 0
    row_count = len(board) + 1
    col_count = len(board[0]) + 1
    
    sum_procession = [[0] * col_count for _ in range(row_count)]
    for skill in skills:
        d = 1
        if (skill[0] == 1):
            d = -1
        
        sum_procession[skill[1]][skill[2]] += d * skill[5]
        sum_procession[skill[3] + 1][skill[4] + 1] += d * skill[5]
        sum_procession[skill[1]][skill[4] + 1] += d * skill[5] * -1
        sum_procession[skill[3] + 1][skill[2]] += d * skill[5] * -1
        
    for row_index in range(row_count):
        value = sum_procession[row_index][0]
        for col_index in range(1, col_count):
            sum_procession[row_index][col_index] += value
            value = sum_procession[row_index][col_index]
            
    for col_index in range(col_count):
        value = sum_procession[0][col_index]
        for row_index in range(1, row_count):
            sum_procession[row_index][col_index] += value
            value = sum_procession[row_index][col_index]    
    
          
    for col_index in range(col_count - 1):
        for row_index in range(row_count - 1):
            board[row_index][col_index] += sum_procession[row_index][col_index]

    
    for row in board:
        for item in row:
            if (item > 0):
                answer += 1

    return answer