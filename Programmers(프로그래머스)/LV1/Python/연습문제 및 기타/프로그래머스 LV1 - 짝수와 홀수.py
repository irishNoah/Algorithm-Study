# 프로그래머스 LV1 - 짝수와 홀수
# https://programmers.co.kr/learn/courses/30/lessons/12937

# 정확성 테스트의 케이스 16개 중 16개 성공
# 효율성 테스트는 없었음
# 총점 100.0점

def solution(num):
    answer = ''

    a, b = divmod(num, 2)

    if b == 0:
        answer = "Even"
    else:
        answer = "Odd"

    return answer

num = 4
print(solution(num))