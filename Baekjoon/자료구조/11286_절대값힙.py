import sys
import heapq

N = int(sys.stdin.readline()) # 연산의 개수(1~100,000)
nums = [int(sys.stdin.readline()) for _ in range(N)] # 연산에 대한 정보를 나타내는 정수들
po_heap = list() # 양수 힙
ne_heap = list() # 음수 힙
for num in nums:
    if num == 0:
        # 리스트에 원소가 없을 때
        if not ne_heap and not po_heap:
            print(0)
        # 음수 힙 리스트에 원소가 없을 때
        elif not ne_heap:
            print(heapq.heappop(po_heap))
        # 양수 힙 리스트에 원소가 없을 때
        elif not po_heap:
            print(-heapq.heappop(ne_heap))
        elif po_heap[0] > ne_heap[0]:
            print(-heapq.heappop(ne_heap))
        elif po_heap[0] < ne_heap[0]:
            print(heapq.heappop(po_heap))
        # 두개의 최소 힙이 같을 때
        else:
            print(-heapq.heappop(ne_heap))
    else:
        if num > 0:
            heapq.heappush(po_heap, num)
        else:
            heapq.heappush(ne_heap, -num)