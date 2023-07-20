# [프로그래머스]-파이썬-내일배움코스-(마법의-엘리베이터)-(1-내풀이-실패)-8점.py
# https://github.com/irishNoah/Algorithm-Study
'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건


*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

'''
#===================================================================================


def solution(storey):
    rock = 0

    leng = len(str(storey))
    c = leng-1

    for x in range(1, c+1):
        left = storey % pow(10, x)
        str_left = str(left)

        # 나머지가 0~5 사이일 때는 내림을 해주는 것이 좋다
        # 예 > 나머지가 20이면 내림으로 0으로 만든다.
        if "0" <= str_left[-1] <= "5":
            rock += left // pow(10, x-1)
            storey -= left
        # 나머지가 6~9 사이일 때는 올림을 해주는 것이 좋다
        # 예 > 나머지가 70이면 올림으로 100으로 만든다.
        else:
            rock += 10 - (left // pow(10, x-1))
            storey += pow(10, x) - left

    rock += storey // pow(10, c)

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