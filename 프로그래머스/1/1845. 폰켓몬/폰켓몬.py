def solution(nums):
    answer = 0
    
    sets = set(nums)
    
    N = len(nums) // 2
    
    # 종류의 갯수 > 선택할 수 있는 갯수
    if len(sets) > N:
        return N
    else :
        return int(str(len(sets))[0:N])
    

