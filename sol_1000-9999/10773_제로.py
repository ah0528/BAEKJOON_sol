import sys
input = sys.stdin.readline
n = int(input())

stack = []
for i in range(n):
    inp = input().split()
    if (int(inp[i]) == 0):
        stack.pop()
    else:
        stack.append()

print(sum(stack))