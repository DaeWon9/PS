import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().rstrip().split())
DNA_list = []
result_string = ''
result_count = 0

for _ in range(N):
    DNA_list.append(sys.stdin.readline().rstrip())


for row in range(M):
    target_list = []
    for col in range(N):
        target_list.append(DNA_list[col][row])

    result = Counter(target_list).most_common()
    max_count = result[0][1]
    dna = []

    for i in range(len(result)):
        if (result[i][1] == max_count):
            dna.append(result[i][0])
    dna = sorted(dna)

    result_string = result_string + dna[0]
    result_count = result_count + (N - max_count)

print(result_string)
print(result_count)