list2 = [1, 1, 2, 2, 2, 8]

x = list(map(int, input().split()))
# print(x)

for i in range(len(list2)):
    print(list2[i] - x[i], end=" ")