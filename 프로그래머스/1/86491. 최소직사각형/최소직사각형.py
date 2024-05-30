def solution(sizes):
    answer = 0

    # List Comprehension
    sorted_arr = [sorted(sub_arr) for sub_arr in sizes]
    
    # 첫 번째 값 리스트
    first_values = [sub_arr[0] for sub_arr in sorted_arr]
    second_values = [sub_arr[1] for sub_arr in sorted_arr]
    
    return max(first_values) * max(second_values)    
    
    
    
