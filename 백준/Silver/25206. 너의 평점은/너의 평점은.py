rate = 0  # 학점의 총합
sum = 0  # (학점 × 과목평점)의 합

# 딕셔너리 자료형
rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for i in range(20):
    subject, score, grade = input().split()
    if grade != "P":
        rate += float(score)
        sum += float(score) * rating[grade]

print(format(sum / rate, ".6f"))
