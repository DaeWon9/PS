n = int(input())

copy_n = n

count = copy_n // 5
copy_n = copy_n % 5

count = count + ( copy_n // 2 )
copy_n = copy_n % 2

case_1 = [count, copy_n]

if (case_1[1] != 1):
    print(case_1[0])
else:
    if ( n // 5 > 0):
        print(case_1[0] + 2)
    else:
        print(-1)
