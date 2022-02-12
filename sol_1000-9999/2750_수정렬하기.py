# 2750_수정렬하기

import sys

input = sys.stdin.readline

result = []

n = int(input())

for _ in range(n):
    a = input()
    result.append(int(a))

len_result = len(result)
for i in range(1, len_result):
    key = result[i]
    j = i - 1
    while j>=0 and result[j] > key:
        result[j+1] = result[j]
        j -= 1
    result[j+1] = key

for i in result:
    print(i)