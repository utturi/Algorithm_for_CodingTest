import sys

city_num = int(sys.stdin.readline()) # 도시의 개수(2~100,000)
length = list(map(int, sys.stdin.readline().split())) # 도로의 길이(1~1,000,000,000)
price = list(map(int, sys.stdin.readline().split())) # 주유소의 리터당 가격(1~1,000,000,000)

standard = price[0] # 첫 도시의 주유소를 기준으로 함
result = 0
for i in range(0, city_num-2):
    if standard <= price[i+1]:
        result += standard * length[i]
    else:
        result += standard * length[i]
        standard = price[i+1]
else:
    result += standard * length[i+1]

# for - else : 반복문 도중 break가 되지 않고 반복문을 끝까지 실행했을 경우 else에 있는 코드를 실행

print(result)