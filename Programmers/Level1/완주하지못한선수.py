## 해싱
 # Dictionary

def solution(participant, completion):
    answer = ''
    hashing = dict()
    p_length = len(participant)
    
    for idx in range(p_length):
        if participant[idx] not in hashing:
            hashing[participant[idx]] = 1
        else:
            hashing[participant[idx]] += 1
    
    for idx in range(p_length-1):
        hashing[completion[idx]] -= 1
        if hashing[completion[idx]] == 0:
            del hashing[completion[idx]]
            
    answer = list(hashing.keys())[0]
    
    return answer