import sys

x = int(sys.stdin.readline().rstrip()) # 정수값(1~30,000)
dp = [0] * (x+1)

dp[1] = 0

for i in range(2, x+1):
    # x에서 1을 빼는 경우
    dp[i] = dp[i-1] + 1
    # x가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # x가 3으로 나누어 떨어지는 경우     
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    # x가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)    

print(dp[x])