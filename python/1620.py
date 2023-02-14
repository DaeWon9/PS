import sys

N, M = map(int, input().split(" "))

pockemon = dict()
reverse_pockemon = dict()

for i in range(N):
    pockemon_name = sys.stdin.readline().rstrip()
    reverse_pockemon[pockemon_name] = i + 1
    pockemon[i + 1] = pockemon_name


for _ in range(M):
    question = sys.stdin.readline().rstrip()
    try:
        question = int(question)
        print(pockemon[question])
    except ValueError:
        print(reverse_pockemon[question])