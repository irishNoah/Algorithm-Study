# 프로그래머스 LV1 - 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884

# 정확성 테스트의 케이스 7개 중 7개 성공
# 효율성 테스트는 없었음
# 총점 100.0

def solution(left, right):
    answer = 0

    for num in range(left, right+1):
        cnt = 0

        for value in range(1, num+1):
            if num % value == 0:
                cnt += 1

        if cnt % 2 == 0:
            answer +=  num

        else :
            answer -= num
 

    return answer

left = 24
right = 27
print(solution(left, right))