# 2753 / 윤년 / B4
# https://www.acmicpc.net/problem/2753

# 연도 입력 받기
year = int(input())

# 윤년이면 1 출력
if (year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0)) :
    print("1")

# 윤년이 아니면 0 출력
else :
    print("0")