import sys

shift_num = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8} # 문자를 숫자로 변환
# ord() - 아스키코드 값을 이용해 숫자로 변환할 수도 있음

location = sys.stdin.readline() # 좌표입력
col = shift_num.get(location[0])
row = int(location[1])

steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)] # 총 8가지의 경우의 수 존재

result = 0
for step in steps:
    n_col = col + step[0]
    n_row = row + step[1]

    if n_col > 0 and n_col < 9:
        if n_row > 0 and n_row < 9:
            result += 1

print(result)