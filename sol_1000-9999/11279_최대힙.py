# 11279_최대힙
import sys
# from queue import PriorityQueue
import heapq

input = sys.stdin.readline
# queue = PriorityQueue()
heap = []
n = int(input())

for _ in range(n):
    inp = int(input())

    if (inp != 0):
        heapq.heappush(heap, -inp)
    else:
        if (len(heap) == 0): # if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))