def solution(arr):
    index = 0
    
    while True:
        # 이전 배열을 저장
        prev = arr[:]
        
        # 배열의 각 원소를 조건에 맞게 변환
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1
        
        index += 1
        
        # 변환된 배열이 이전 배열과 같은지 확인
        if prev == arr:
            break
    
    return index - 1
