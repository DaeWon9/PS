import sys

A = int(sys.stdin.readline())
T = int(sys.stdin.readline())
B = int(sys.stdin.readline())

pupa_string = ''

repeat_count = 1
temp = T
c = 4

while(True):
    if (temp <= c):
        break
    c = c + repeat_count
    repeat_count += 1

for i in range(1, repeat_count+1):
    pupa_string = pupa_string + '0101' + '0' * (i + 1) + '1' * (i + 1)

count = 0
target_index = 0
for i in range(len(pupa_string)):
    if (int(pupa_string[i]) == B):
        count += 1
    
    if (count == T):
        target_index = i
        break

print(target_index % A)