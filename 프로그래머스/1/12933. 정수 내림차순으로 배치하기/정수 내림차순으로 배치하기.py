def solution(n):

    li=list(str(n))
    li.sort(reverse=True)
    sorted_n="".join(li)
    return int(sorted_n)
