def solution(s, n):
    answer = ''
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for char in s:
        if char in low:
            index = low.find(char)+n
            answer += low[index%26]
        elif char in up:
            index = up.find(char)+n
            answer += up[index%26]
        else:
            answer += " "
            
    
    return answer
    
