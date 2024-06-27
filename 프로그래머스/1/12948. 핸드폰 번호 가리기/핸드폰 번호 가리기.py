def solution(phone_number):
    back = phone_number[-4:]
    return "*" * int(len(phone_number) - 4) + back