def solution(phone_book):
    phone_book.sort()  # 정렬을 통해 효율성 향상
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True