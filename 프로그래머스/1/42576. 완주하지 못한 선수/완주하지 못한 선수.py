from collections import Counter

def solution(participant, completion):
    # 참가자와 완주자의 이름을 카운트
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    # 두 카운터의 차이를 계산
    difference = participant_count - completion_count
    
    # 차이가 나는 이름을 반환 (완주하지 못한 선수)
    return list(difference.keys())[0]