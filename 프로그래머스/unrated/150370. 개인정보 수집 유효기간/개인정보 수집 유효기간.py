def is_destroy(t_value, privacy, period):
    p_year, p_month, p_day = privacy.split('.')
    p_year = int(p_year)
    p_month = int(p_month)
    p_day = int(p_day)
    
    p_month += int(period)
    if (p_month > 12):
        p_month -= 12
        p_year += 1

    p_value = p_year * 12 * 28 + p_month * 28 + p_day
    return (t_value >= p_value)
    

def solution(today, terms, privacies):
    answer = []
    term_dict = dict()
    t_year, t_month, t_day = today.split('.')
    t_value = int(t_year) * 12 * 28 + int(t_month) * 28 + int(t_day)
    
    for term in terms:
        key, value = term.split()
        term_dict[key] = value
        
    for index in range(1, len(privacies)+1):
        date, key = privacies[index - 1].split()
        if (is_destroy(t_value, date, term_dict[key])):
            answer.append(index)
        
    return answer