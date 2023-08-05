from collections import defaultdict
import math

max_time = 60 * 23 + 59

def solution(fees, records):
    min_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    record_dict = defaultdict(int)
    result_dict = defaultdict(int)
    
    answer = []
    for record in records:
        splited_record = record.split()
        time = splited_record[0]
        car_number = splited_record[1]
        status = splited_record[2]
        
        converted_time = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
        if(status == "IN"):
            record_dict[car_number] = max_time - converted_time
        else: # out
            result_dict[car_number] += converted_time - max_time + record_dict[car_number]
            record_dict[car_number] = 0
    
    sorted_record = sorted(record_dict.items())

    for car in sorted_record:
        final_time = record_dict[car[0]] + result_dict[car[0]]
        if (final_time <= min_time):
            answer.append(default_fee)
        else:
            final_time = math.ceil((final_time - min_time) / unit_time)
            answer.append(default_fee + final_time * unit_fee)
            
    return answer