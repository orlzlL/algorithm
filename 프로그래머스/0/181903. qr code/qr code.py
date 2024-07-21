def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer += "".join(code[i])
    return answer