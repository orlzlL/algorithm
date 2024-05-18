def solution(arr):
    answer = []
    
    arr.remove(min(arr))
    answer = arr
    
    if not arr:
        return [-1]
    
    
    return answer