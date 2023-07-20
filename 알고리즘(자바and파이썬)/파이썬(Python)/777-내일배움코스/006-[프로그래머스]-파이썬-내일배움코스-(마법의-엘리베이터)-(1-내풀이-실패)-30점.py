# [프로그래머스]-파이썬-내일배움코스-(마법의-엘리베이터)-(1-내풀이-실패)-30점.py
# https://github.com/irishNoah/Algorithm-Study
'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건


*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

'''
#===================================================================================


def solution(storey):
    rock = 0

    storey = str(storey)

    for x in range(len(storey)-1, -1, -1):
        if "0" <= storey[x] <= "5":
            rock += int(storey[x])
        else:
            rock += (10-int(storey[x])+1)

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