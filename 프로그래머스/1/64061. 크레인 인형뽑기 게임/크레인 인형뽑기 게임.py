def solution(board, moves):
    answer = 0
    stack = []
    
    for move in moves:
        target_col = move - 1
        
        for row_index in range(len(board)):
            if (board[row_index][target_col] != 0):
                stack.append(board[row_index][target_col])
                board[row_index][target_col] = 0
                
                
                if (len(stack) > 1 and stack[-1] == stack[-2]):
                    stack.pop()
                    stack.pop()
                    answer += 2
                break

    return answer