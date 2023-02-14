import sys

M = int(input())
S = set()

for i in range(M):
    print(S)
    
    inputData = sys.stdin.readline().rstrip()

    if inputData == 'all':
        S = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif inputData == 'empty':
        S = set()
    else:
        function, value = inputData.split(" ")
        value = int(value)
        if function == 'add':
            if value not in S:
                S.add(value)
        elif function == 'remove':
            if value in S:
                S.remove(value)
        elif function == 'check':
            if value in S:
                print(1)
            else:
                print(0)
        elif function == 'toggle':
            if value in S:
                S.remove(value)
            else:
                S.add(value)