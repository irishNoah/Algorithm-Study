# 10950 / A+B - 3 / B3
# https://www.acmicpc.net/problem/10950

# 테스트 케이스 총 개수 변수 case 선언 후 입력 받기
case = int(input())

for i in range(case) :
    # 정수 2개를 list 형식으로 입력받기
    a, b = list(map(int, input().split()))

    # 두 정수에 대한 합산을 구하고 출력하기
    sum = a+b
    print(sum)