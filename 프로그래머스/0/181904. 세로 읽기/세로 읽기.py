def solution(my_string, m, c):
    answer = ''
    arr = []
    
    for i in range(0, len(my_string), m):
        arr.append(my_string[i : i + m])
        
    for j in arr:
        answer += j[c - 1]
        
        
    return answer