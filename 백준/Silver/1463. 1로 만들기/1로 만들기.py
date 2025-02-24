import sys
input = sys.stdin.readline

X = int(input())
leaf = { X }
count = 0

if (X == 1):
    pass
else:
    while(1 not in leaf):
        children = set()
        for node in leaf:
            if (node % 3 == 0):
                children.add(node // 3)
            if (node % 2 == 0):
                children.add(node // 2)
            children.add(node - 1)
        
        leaf = children
        count = count + 1

print(count)