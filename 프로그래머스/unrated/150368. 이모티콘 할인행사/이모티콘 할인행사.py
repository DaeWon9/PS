from itertools import product

def solution(users, emoticons):
    answer = []
    all_answer = []
    max_user_count = 0
    discount_rates = (10, 20, 30, 40)

    for discount_rate in list(product(discount_rates, repeat = len(emoticons))):
        emoticons_plus_user_count = 0
        result_cost_sum = 0
        for user_discount_rate, max_cost in users:

            discounted_cost_sum = 0
            for cost, rate in zip(emoticons, discount_rate):
                if (rate >= user_discount_rate):
                    discounted_cost_sum += int((100 - rate) * cost / 100)

            if (discounted_cost_sum >= max_cost):
                emoticons_plus_user_count += 1
            else:
                result_cost_sum += discounted_cost_sum
            
        max_user_count = max(max_user_count, emoticons_plus_user_count)
        
        if (emoticons_plus_user_count >= max_user_count):
            all_answer.append((emoticons_plus_user_count, result_cost_sum))
        
    all_answer.sort(key=lambda x: (-x[0], -x[1]))
    answer = all_answer[0]
    return answer