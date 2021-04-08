import sys

N, K = map(int, sys.stdin.readline().split()) # N, K : 2~100,000

cnt = 0 # 횟수 변수
while N != 1: # 1이 될 때까지 반복
    if N % K == 0:
        N //= K
    else:
        N -= 1

    cnt += 1

print(cnt)