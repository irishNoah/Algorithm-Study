# 프로그래머스 LV1 - 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934

# 정확성 테스트의 케이스 18개 중 18개 성공
# 효율성 테스트는 없었음
# 총점 100.0점

import math

def solution(n):
    answer = 0

    value = math.sqrt(n)

    if value % 1 == 0:
        answer = int(pow(value+1, 2))

    else :
        answer = -1

    return answer

n = 121
print(solution(n))