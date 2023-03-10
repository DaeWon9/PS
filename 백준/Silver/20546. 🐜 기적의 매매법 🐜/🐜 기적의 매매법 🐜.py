import sys

money = int(sys.stdin.readline())
stock_price_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

JH_money = money
SM_money = money
JH_stock_count = 0
SM_stock_count = 0

for price in stock_price_list:
    if (JH_money >= price):
        JH_stock_count = JH_stock_count + (JH_money//price)
        JH_money = JH_money % price
    
for i in range(3,14):
    if (stock_price_list[i-1] < stock_price_list[i-2] and stock_price_list[i-2] < stock_price_list[i-3]): # 3일 연속 하락 시 매수
        SM_stock_count = SM_stock_count + (SM_money//stock_price_list[i])
        SM_money = SM_money % stock_price_list[i]

    if (stock_price_list[i-1] > stock_price_list[i-2] and stock_price_list[i-2] > stock_price_list[i-3]): # 3일 연속 상승 시 매도
        SM_money = SM_money + (stock_price_list[i] * SM_stock_count)
        SM_stock_count = 0

JH_result = JH_money + JH_stock_count * stock_price_list[13]
SM_result = SM_money + SM_stock_count * stock_price_list[13]

if (JH_result > SM_result):
    print("BNP")
elif (JH_result < SM_result):
    print("TIMING")
else:
    print("SAMESAME")