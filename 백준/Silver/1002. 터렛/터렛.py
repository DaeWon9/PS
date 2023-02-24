import math

repeat = int(input())

for i in range (repeat):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))
    centor_pointer_distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if (x1 == x2 and y1 == y2 and r1 == r2 ): #똑같은 원
        print(-1)
    elif (centor_pointer_distance == r1 + r2): #외접
        print(1)
    elif (centor_pointer_distance == abs(r1 - r2)): #내접
        print(1)
    elif (centor_pointer_distance > abs(r1 - r2) and centor_pointer_distance < (r1+r2)): # 두 교점
        print(2)
    else: # 그 외에는 만나지 않음
        print(0)