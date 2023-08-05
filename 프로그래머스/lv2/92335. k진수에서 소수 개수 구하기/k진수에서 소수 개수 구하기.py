import math

def convert_base(n, k):
    result = ""
    
    while n > 0:
        result = str(n % k) + result
        n //= k
        
    return result

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if(n % i == 0):
                return False
        return True

def solution(n, k):
    answer = 0
    splited_by_zero = convert_base(n,k).split('0')
    for number in splited_by_zero:
        if (number != "" and is_prime(int(number))):
            answer += 1
            
    return answer