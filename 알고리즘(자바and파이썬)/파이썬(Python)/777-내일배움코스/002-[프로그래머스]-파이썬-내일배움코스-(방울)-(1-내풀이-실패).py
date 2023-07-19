# [프로그래머스]-파이썬-내일배움코스-(방울)-(1-내풀이-실패).py
# https://github.com/irishNoah/Algorithm-Study
'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건
>>> 1 <= bell의 길이 <= 1000000
>>> 1 <= bell[i] <= 2
>>> bell[i]가 1은 빨간색 장식을, bell[i]가 2는 초록색 장식을 의미한다.

*** 설계 [총 26분 소요] / 총 풀이 시간[총 ?분 소요]
- 음... 갯수가 같고, 둘 중 하나라도 0인거는 생각해서 하겠는데 다를 때는 어케 해야 할지 ㅎㅎ

'''
#===================================================================================


def solution(bell):
    answer = 0

    cntOne = bell.count(1); cntTwo = bell.count(2);

    # 갯수가 같다면 그냥 2배가 정답
    if cntOne == cntTwo:
        answer = cntOne*2
    # 둘 중 하나라도 0이면 답도 0
    elif cntOne == 0 or cntTwo == 0:
        answer = 0

    return answer

#===================================================================================

# bell = [1,2,1,1,1,2,2,1]
# print(solution(bell)) # 6

# bell = [1,2,1,2,1,2,1,2]
# print(solution(bell)) # 8

# bell = [1,1,1,1,1,1]
# print(solution(bell)) # 0

bell = [2,2,1,1,2,2,2,2,2,2,1]
print(solution(bell)) # 4

# def solution(bell):
#     answer = 0
#     return answer