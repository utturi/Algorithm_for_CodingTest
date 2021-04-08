import sys

N, M = map(int, sys.stdin.readline().split()) # N x M 행렬(1~100)
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # N개 줄만큼의 숫자(1~10,000)

check = [0 for _ in range(N)] # N개의 행을 탐색 후, 다음행의 min()값을 넣는 리스트
for i in range(N):
    if i == N-1:
        check[i] = min(nums[0])
    else:
        check[i] = min(nums[i+1])

print(max(check))