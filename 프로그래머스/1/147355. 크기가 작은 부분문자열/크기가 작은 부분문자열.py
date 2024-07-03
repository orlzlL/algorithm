def solution(t, p):
    answer = 0
    len_p = len(p)
    int_p = int(p)
    
    for i in range(len(t) - len_p + 1):
        tmp = t[i:i + len_p]
        if int(tmp) <= int_p:
            answer += 1
            
    return answer
