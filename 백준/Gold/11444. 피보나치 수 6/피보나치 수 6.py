import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# ( Fn+1 Fn   )  =  ( 1 1 ) ^n
# ( Fn   Fn-1 )     ( 1 0 )

def multiply_matrix(matrix1, matrix2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k] * matrix2[k][j] % 1000000007
    return result

# 분할정복
def power_matrix(base_matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:  # b의 값이 1이 될 때까지 재귀
        return base_matrix
    else:
        temp = power_matrix(base_matrix, n // 2)
        if n % 2 == 0:
            return multiply_matrix(temp, temp)
        else:
            return multiply_matrix(multiply_matrix(temp, temp), base_matrix)

base_matrix = [[1, 1], [1, 0]]
n = int(input())

result_matrix = power_matrix(base_matrix, n-1)
print(result_matrix[0][0] % 1000000007)