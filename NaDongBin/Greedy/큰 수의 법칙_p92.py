import sys

N, M, K = map(int, sys.stdin.readline().split()) # N : 2~1,000, M : 1~10,000, K : 1~10,000
nums = list(map(int, sys.stdin.readline().split())) # 각각의 수 : 1~10,000

nums = sorted(nums, reverse=True) # 내림차순 정렬
i = 0 # K번 초과하여 더해질 수 없도록 검사하는 변수
total = 0
for _ in range(M):
    if i == K:
        i = 0
        total += nums[1]
    else:
        i += 1
        total += nums[0]

print(total)