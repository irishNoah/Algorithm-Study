# 프로그래머스 LV1 - 두 정수 사이의 합(초기풀이)
# 분류 - 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12912

# 정확성 테스트의 케이스 16개 중 16개 성공
# 효율성 테스트는 없었음
# 총점 100.0

def solution(a, b):
    answer = 0

    if a == b:
        answer = a
        return answer

    if b < a :
        x = a
        a = b
        b = x

    for i in range(a, b+1):
        answer += i

    return answer

a = 5
b = 3
print (solution(a, b))
