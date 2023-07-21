# [프로그래머스]-파이썬-내일배움코스-(마법의-엘리베이터)-(4-내풀이)-유사풀이복습.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/148653
'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

'''
#===================================================================================


def solution(storey):
    rock = 0

    while True:

        left = storey % 10

        # 5와 같을 때, 미만일 때, 초과일 때로 구분한다.
        if left < 5:
            rock += left
            storey -= left
        elif left > 5:
            rock += (10-left)
            storey += (10-left)
        else:
            rock += left
            mok = storey // 10

            # 몫의 마지막 수가 5미만이면 차감, 이상이면 증가 시켜준다.
            # 예 : 252(5) >>> 250 / 256(5) >>> 260
            if mok % 10 < 5:
                storey -= left
            else:
                storey += left

        if storey == 0:
            break
        storey = storey // 10

    return rock
#===================================================================================

# 예제 1
storey = 16
print(solution(storey)) # 6

# 예제 2
storey = 2554
print(solution(storey)) # 16

# def solution(storey):
#     answer = 0
#     return answer