def solution(brown, yellow):
    for bh in range(1, brown//2 + 1):
        bw = (brown - 2 * bh + 4) // 2
        yh, yw = bh - 2, bw - 2
        if yellow == yh * yw and yellow + brown == bh * bw:
           return [bw, bh]