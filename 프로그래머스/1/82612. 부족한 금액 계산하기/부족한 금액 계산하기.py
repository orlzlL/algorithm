def solution(price, money, count):
    
    # 필요한 금액 
    temp = 0
    
    for i in range(1, count + 1):
        temp += price * i

    if (money - temp) < 0:
        return abs(money - temp)
    else :
        return 0
        
