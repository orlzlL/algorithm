from itertools import product

def solution(clothes):
    answer = 1
    dict1 = dict()
    
    for item, category in clothes:
        if category not in dict1:
            dict1[category] = []
        dict1[category].append(item)

    counts = [len(items) + 1 for items in dict1.values()]
    for i in range(len(counts)):
        answer *= counts[i]


    return answer - 1