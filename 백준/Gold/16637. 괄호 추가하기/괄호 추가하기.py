import sys
input = sys.stdin.readline

# 3+8×7-9×2
# 단, 괄호 안에는 연산자가 하나만 들어 있어야 한다.
# 연속된 연산자는 괄호로 묶지 못함.
# combination 을 구할 때, 시작 index부터 2이상인 index를 넣어서 구하고
# 각 수식을 계산하여, 최댓값 출력

def calc(operator, left_operand, right_operand):
    if (operator == '+'):
        return left_operand + right_operand
    elif (operator == '-'):
        return left_operand - right_operand
    else:
        return left_operand * right_operand

def combinations(start = 0, path:list = [], result:list = []):
    if (path):
        result.append(path[:])

    for i in range(start, operator_count):
        path.append(i)
        combinations(i + 2, path, result)
        path.pop()

    return result

N = int(input())
operator_count = N // 2
operators = []
operands = []
answer = -2147483647
for i, data in enumerate(input().rstrip()):
    if (i % 2 == 0): # operand
        operands.append(int(data))
    else:
        operators.append(data)

if (N == 1):
    print(operands[0])
    exit(0)

for combi in combinations():
    copied_operands = operands[:]
    copied_operators = operators[:]

    for idx in sorted(combi, reverse=True):
        copied_operands[idx] = calc(copied_operators[idx], copied_operands[idx], copied_operands[idx + 1])
        del copied_operands[idx + 1]
        del copied_operators[idx]

    result = copied_operands[0]
    for i, op in enumerate(copied_operators):
        result = calc(op, result, copied_operands[i + 1])

    answer = max(answer, result)

print(answer)