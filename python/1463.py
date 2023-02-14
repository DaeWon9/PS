X = int(input())

leaf = [X]

count = 0
if (X == 1):
    pass
else:
    while(1 not in leaf):
        parent = leaf
        children = []
        for node in parent:
            if (node % 3 == 0):
                children.append(node / 3)
            if (node % 2 == 0):
                children.append(node / 2)
            children.append(node - 1)
        
        leaf = children
        count = count + 1

print(count)