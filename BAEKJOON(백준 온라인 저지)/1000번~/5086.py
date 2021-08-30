# 5086 / 배수와 약수 / B3
# https://www.acmicpc.net/problem/5086

while True :
    a, b = map(int, input().split())

    # 만약 입력받는 두 숫자 모두 0이면 강제 종료
    if a == 0 and b == 0 :
        break

    # b를 a로 나눈 나머지가 0이라면 a는 b의 약수이므로
    # factor 출력
    if b % a == 0 :
        print("factor")

    # a를 b로 나눈 나머지가 0이라면 a는 b의 배수이므로
    # multiple 출력
    elif a % b == 0 :
        print("multiple")

    # 위 2가지 경우가 아니라면 약수와 배수 모두 아니므로
    # neither을 출력
    else :
        print("neither")