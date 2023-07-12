# [프로그래머스]-파이썬-연습-(평행)-LV0-(2-참고-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/120814

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건
>>> 1 ≤ n ≤ 100

* 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- 

* 나와의 차이
- 난, 조합으로 풀려했다. 하지만, nC2는 그냥 4개의 정보 중 2개씩 묶은 경우를 반환해주지
나머지 2개를 묶어주지는 않는다.
    - 우선, 여기서 멍 때림
- 이 친구는 또 다른 사용자 정의 함수를 구하여 적용했다.

'''
#===================================================================================

def solution(dots):
    answer = 0
    if slope(dots[0],dots[1]) == slope(dots[2],dots[3]):
        answer = 1
    if slope(dots[0],dots[2]) == slope(dots[1],dots[3]):
        answer = 1
    if slope(dots[0],dots[3]) == slope(dots[1],dots[2]):
        answer = 1
    return answer

def slope(dot1,dot2):
    return (dot2[1] - dot1[1] ) / (dot2[0] - dot1[0]) # 기울기 계산 (y축 차이 - x축 차이)


# #############################################################

dots = [[1, 4], [9, 2], [3, 8], [11, 6]]
print(solution(dots)) # 1