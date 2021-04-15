""" DP 문제인데 도저히 DP로 안풀려서 규칙을 찾아서 꿰맞춰서 품
    DP로 다시 풀어볼 것! """
import sys

t_case = int(sys.stdin.readline().rstrip()) # 테스트케이스 개수(최대 100개)
make = {2:1, 3:7, 4:4, 5:2, 6:6, 7:8} # 고정된 값

for _ in range(t_case):
    n = int(sys.stdin.readline().rstrip()) # 성냥개비 개수(2~100)

    # 가장 작은 수
    cnt = (n - 1) // 7
    if n == 6:
        small = 6
    elif n <= 7:
        small = make[n]
    else:
        if n % 7 == 1:
            small = int("10" + ("8" * ((n // 7) - 1)))
        elif n % 7 == 3:
            if n == 10:
                small = 22
            else:
                small = int("200" + ("8" * ((n // 7) - 2)))
        elif n % 7 == 4:
            small = int("20" + ("8" * ((n // 7) - 1)))
        else:
            small = int(str(make[n - (7 * cnt)]) + ("8" * cnt))

    # 가장 큰 수
    cnt = n // 2
    if n % 2 == 0:
        big = int("1" * cnt)
    else:
        big = int("7" + ("1" * (cnt-1)))
    
    print(small, big)