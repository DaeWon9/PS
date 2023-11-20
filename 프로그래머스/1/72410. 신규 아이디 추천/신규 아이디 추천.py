import re

def solution(new_id):
    #step1
    new_id = new_id.lower()

    #step 2
    new_id = re.sub(r'[^a-z0-9\-_\.]', '', new_id)    
    
    #step 3
    while(True):
        if (".." in new_id):
            new_id =  new_id.replace("..",".")
        else:
            break
    
    #step 4
    new_id = new_id.lstrip('.')
    new_id = new_id.rstrip('.')
    
    #step 5
    if (new_id == ''):
        new_id = 'a'
 
    #step 6
    if (len(new_id) >= 16):
        new_id = new_id[0:15]
        new_id = new_id.rstrip('.')

    #step 7
    if (len(new_id) <= 2):
        added_char = new_id[-1]
        while(True):
            if(len(new_id) >= 3):
                break
            new_id += added_char

    answer = new_id
    return answer