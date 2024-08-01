def solution(dartResult):
    temp = []
    result = list(dartResult)
    
    i = 0
    while i < len(result):
        if result[i].isdigit():
            if i + 1 < len(result) and result[i + 1].isdigit():  # '10' 처리
                temp.append(10)
                i += 1
            else:
                temp.append(int(result[i]))
            i += 1

            # 보너스 처리
            if result[i] == 'S':
                temp[-1] = temp[-1] ** 1
            elif result[i] == 'D':
                temp[-1] = temp[-1] ** 2
            elif result[i] == 'T':
                temp[-1] = temp[-1] ** 3
            i += 1
            
        if i < len(result) and result[i] == '*':
            if len(temp) > 1:
                temp[-1] *= 2
                temp[-2] *= 2
            else:
                temp[-1] *= 2
            i += 1
            
        elif i < len(result) and result[i] == '#':
            temp[-1] *= -1
            i += 1
        
    return sum(temp)

# 테스트
print(solution("1S2D*3T"))  # 37
print(solution("1D2S#10S"))  # 9
print(solution("1D2S0T"))  # 3
print(solution("1S*2T*3S"))  # 23
print(solution("1D#2S*3S"))  # 5
print(solution("1T2D3D#"))  # -4
print(solution("1D2S3T*"))  # 59
