import re

def solution(s):
    answer = ''
    p = re.compile('[a-z]+')
    p2 = re.compile('[0-9]+')
    
    i = 0
    while i < len(s):
        if s[i] == ' ':
            answer += ' '
            i += 1
        elif p.match(s[i]):
            answer += s[i].upper()
            i += 1
            while i < len(s) and s[i] != ' ':
                answer += s[i].lower()
                i += 1
        elif p2.match(s[i]):
            answer += s[i]
            i += 1
            while i < len(s) and s[i] != ' ':
                answer += s[i].lower()
                i += 1
        else:
            answer += s[i].upper()
            i += 1
            while i < len(s) and s[i] != ' ':
                answer += s[i].lower()
                i += 1

    return answer