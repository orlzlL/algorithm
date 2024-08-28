import sys

input = sys.stdin.readline
MAX = 10**6 + 1

student_map = [0] * (MAX + 1)


def map_student():
  for _ in range(int(input())):
    start, end = map(int, input().split())
    student_map[start] += 1
    student_map[end+1] -= 1
  for i in range(1, MAX + 1):
    student_map[i] += student_map[i - 1]


def query():
  Q = int(input())
  for q in map(int, input().split()):
    print(student_map[q])


if __name__ == "__main__":
  map_student()
  query()
