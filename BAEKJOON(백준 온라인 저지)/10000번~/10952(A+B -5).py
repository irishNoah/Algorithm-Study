# 10952 / A+B - 5 / B3
# https://www.acmicpc.net/problem/10952

# 이 문제는 테스트케이스의 개수가 명시되어 있지 않으므로
# 언제까지 입력을 받을 줄 모른다.
# 하지만 마지막 줄에 두 정수 모두 0이면 종료된다고 명시하므로
# 두 정수 모두가 0이 아니면 두 수를 합산한 수를 출력하고
# 두 정수가 모두 0이라면 while문을 종료하면 된다.
while True :
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    else :
        print(a+b)