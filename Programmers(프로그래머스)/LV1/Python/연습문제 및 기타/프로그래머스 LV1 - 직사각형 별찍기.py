# 프로그래머스 LV1 - 직사각형 별찍기
# 분류 - 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12969

# 정확성 테스트의 케이스 11개 중 11개 성공
# 효율성 테스트는 없었음
# 총점 100.0


a, b = map(int, input().strip().split(' '))

answer = "*" * a

for i in range(0, b):
    print(answer)