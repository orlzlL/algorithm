n = int(input())
count = 0

for _ in range(n):
    word = input()
    is_group_word = True  # 그룹 단어인지 여부를 저장하는 변수입니다.

    # 각 문자에 대해 인접한 문자와 비교하여 그룹 단어 여부를 확인합니다.
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:  # 현재 문자와 다음 문자가 다르면
            if word[i] in word[i + 1:]:  # 현재 문자 이후에 똑같은 문자가 있는지 확인합니다.
                is_group_word = False
                break

    if is_group_word:
        count += 1

print(count)
