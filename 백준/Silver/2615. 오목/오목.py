import sys

concave_list = []

def check_right(array, target, row, col):
    cnt = 1
    for i in range(1,6):
        if (col+i > 18):
            break
        if (array[row][col+i] == target):
            cnt = cnt + 1
        else:
            break
    
    if (cnt == 5):
        if (col - 1 > -1 and array[row][col - 1] == target):
            return [False, row, col]
        return [True, row, col]
    return [False, row, col]

def check_bottom(array, target, row, col):
    cnt = 1
    for i in range(1,6):
        if (row + i > 18):
            break
        if (array[row+i][col] == target):
            cnt = cnt + 1
        else:
            break
    
    if (cnt == 5):
        if (row - 1 > -1 and array[row - 1][col] == target):
            return [False, row, col]
        return [True, row, col]
    return [False, row, col]

def check_right_bottom(array, target, row, col):
    cnt = 1
    for i in range(1,6):
        if (row + i > 18 or col + i > 18):
            break
        if (array[row+i][col+i] == target):
            cnt = cnt + 1
        else:
            break
    
    if (cnt == 5):
        if (col - 1 > -1 and row - 1 > -1 and array[row - 1][col - 1] == target):
            return [False, row, col]
        return [True, row, col]
    return [False, row, col]

def check_right_top(array, target, row, col):
    cnt = 1
    for i in range(1,6):
        if (row - i < 0 or col + i > 18):
            break
        if (array[row-i][col+i] == target):
            cnt = cnt + 1
        else:
            break
    
    if (cnt == 5):
        if (col - 1 > -1  and row + 1 < 19 and array[row + 1][col - 1] == target):
            return [False, row, col]
        return [True, row, col]
    return [False, row, col]

is_complete = False

for _ in range(19):
    concave_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

for row in range(19):
    if (is_complete):
        break
    for col in range(19):
        if (concave_list[row][col] == 1): #흰 오, 아, 오아, 오위 체크해야함
            if (check_bottom(concave_list, 1, row, col)[0] or check_right(concave_list, 1, row, col)[0] or check_right_bottom(concave_list, 1, row, col)[0] or check_right_top(concave_list, 1, row, col)[0] ):
                print(1)
                print(row + 1, col + 1)
                is_complete = True
                break
        elif (concave_list[row][col] == 2): #검
            if (check_bottom(concave_list, 2, row, col)[0] or check_right(concave_list, 2, row, col)[0] or check_right_bottom(concave_list, 2, row, col)[0] or check_right_top(concave_list, 2, row, col)[0] ):
                print(2)
                print(row + 1, col + 1)
                is_complete = True
                break

if(not is_complete):
    print(0)