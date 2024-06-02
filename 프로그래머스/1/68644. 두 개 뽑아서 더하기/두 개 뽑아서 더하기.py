def solution(numbers):
    answer = []
    temp = 0
    
    for i in range(len(numbers)): 
        for j in range(i + 1, len(numbers)):
            temp = numbers[i] + numbers[j]
            if temp not in answer:
                answer.append(temp)
            
    answer.sort()
    
    return answer