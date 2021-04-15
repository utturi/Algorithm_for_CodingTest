import sys

N = int(sys.stdin.readline().rstrip()) # 정수값(1~1,000,000)
dp = [0] * (N+1)

for i in range(2, N+1):
    # x에서 1을 빼는 경우
    dp[i] = dp[i-1] + 1

    # x가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
        
    # x가 3로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    
print(dp[N])