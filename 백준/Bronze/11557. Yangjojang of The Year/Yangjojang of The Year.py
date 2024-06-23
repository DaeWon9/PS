import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    max_amount = 0
    answer_school_name = ""

    N = int(input())

    for _ in range(N):
        school_name, amount = map(str, input().rstrip().split())
        amount = int(amount)

        if (max_amount < amount):
            max_amount = amount
            answer_school_name = school_name

    print(answer_school_name)