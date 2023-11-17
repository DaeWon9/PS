def solution(s):
    answer = ""
    
    for i in range(len(s)):
        if (s[i].isdigit()):
            answer += s[i]
            continue
        
        if (s[i] == 'z'): # zero
            if (i+1 < len(s) and s[i+1] == 'e'):
                answer += '0'
        elif (s[i] == 'o'): # one
            if (i+1 < len(s) and s[i+1] == 'n'):
                answer += '1'
        elif (s[i] == 't'): # two, three
            if (i+1 < len(s) and s[i+1] == 'w'):
                answer += '2'
            if (i+1 < len(s) and s[i+1] == 'h'):
                answer += '3'
        elif (s[i] == 'f'): # four, five
            if (i+1 < len(s) and s[i+1] == 'o'):
                answer += '4'
            elif (i+1 < len(s) and s[i+1] == 'i'):
                answer += '5'
                
        elif (s[i] == 's'): # six, seven
            if (i+1 < len(s) and s[i+1] == 'i'):
                answer += '6'
            elif (i+1 < len(s) and s[i+1] == 'e'):
                answer += '7'
        elif (s[i] == 'e'): # eight 
            if (i+1 < len(s) and s[i+1] == 'i'):
                answer += '8'
        elif (s[i] == 'n'): # nine
            if (i+1 < len(s) and s[i+1] == 'i'):
                answer += '9'
            
        
        

    
    
    
    return int(answer)