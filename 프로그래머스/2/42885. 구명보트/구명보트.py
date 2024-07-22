def solution(people, limit):
    people.sort()  # 오름차순으로 정렬
    answer = 0
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    
    return answer