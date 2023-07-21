# [프로그래머스]-파이썬-내일배움코스-(마법의-엘리베이터)-(3-강사풀이)-재귀.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/148653
'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

*** 강사 풀이
뒷자리가 0인 수는 0을 빼도 누르는 버튼수가 같습니다.
(뒤가 0이면 +-1 버튼을 누를 일이 없으므로 /10버튼을 누르면 결국 같음.)
따라서 자리수 단위로 감소하는 재귀로 접근하면 쉽게 해결할 수 있습니다.
예를 들어 solution(2554)는 solution(255) + 4 와 solution(256) + 6 둘 중 더 적은쪽일것입니다.
solution(255) + 4은 -1을 4번 하고 2550을 만든 경우고,
solution(256) + 6은 +1을 6번하고 2560을 만든 경우입니다.

'''
#===================================================================================


def solution(storey):
    if storey <= 1:
        return storey
    q, r = divmod(storey, 10)
    return min(solution(q) + r, solution(q+1) + (10-r) )


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