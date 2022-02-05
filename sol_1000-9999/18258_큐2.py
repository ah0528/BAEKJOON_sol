import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

n = int(input())

for _ in range(n):
    inp = input().split()
                                                                                                                                                                                             
    if (inp[0] == 'push'):
        queue.append(inp[1])

    elif (inp[0] == 'pop'):
        if (len(queue) == 0):
            print(-1)
        else:
            data = queue.popleft()
            print(data)

    elif (inp[0] == 'size'):
        print(len(queue))

    elif (inp[0] == 'empty'):
        if (len(queue) == 0):
            print(1)
        else:
            print(0)

    elif (inp[0] == 'front'):
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue[0])

    elif (inp[0] == 'back'):
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue[-1])