# sort함수로 해보기

import sys

input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    a = input().strip()
    lst.append(int(a))

b = sorted(lst)
for i in b:
    print(i)