# 4153번 / 직각삼각형 / B3
# https://www.acmicpc.net/problem/4153

while 1:
    # a, b, c 변수에 입력
    a, b, c = map(int, input().split())

    # 종료 조건
    if a == 0 and b == 0 and c == 0:
        break

    # list_value라는 리스트 생성
    list_value = []

    # a, b, c를 차례대로 list_value에 append하기
    list_value.append(a)
    list_value.append(b)
    list_value.append(c)

    # list_value 오름차순 정렬
    # 그렇게 하는 이유는 a b c 순대로 정렬되어 있다는 보장이 없기 때문
    # 왜 이렇게 해야 하는지는 직각삼각형의 원리를 보면 이해할 수 있음
    list_value = sorted(list_value)

    # 각 list_value의 요소 제곱한 것을 pow_1 ~ pow_3에 차례대로 할당
    # 참고로 list_value[2]가 입력 요소 중 가장 큰 값에 해당
    pow_1 = pow(list_value[0], 2)
    pow_2 = pow(list_value[1], 2)
    pow_3 = pow(list_value[2], 2)

    # 직각삼각형의 공식은 (대각선의 길이의 제곱) = (가로의 제곱) + (세로의 제곱)이기 때문에
    # 해당 공식에 부합하면 right를, 그렇지 않은 경우에는 wrong을 출력
    if pow_3 == pow_1 + pow_2:
        print("right")

    else:
        print("wrong")