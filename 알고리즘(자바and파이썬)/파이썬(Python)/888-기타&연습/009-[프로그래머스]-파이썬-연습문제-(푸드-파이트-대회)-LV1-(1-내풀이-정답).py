# [프로그래머스]-파이썬-연습문제-(푸드-파이트-대회)-LV1-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/134240

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건
>>> 2 ≤ food의 길이 ≤ 9
>>> 1 ≤ food의 각 원소 ≤ 1,000
>>> food에는 칼로리가 적은 순서대로 음식의 양이 담겨 있습니다.
>>> food[i]는 i번 음식의 수입니다.
>>> food[0]은 수웅이가 준비한 물의 양이며, 항상 1입니다.
>>> 정답의 길이가 3 이상인 경우만 입력으로 주어집니다.

*** 설계 [총 11분 소요] / 총 풀이 시간[총 14분 소요]
>>> for문 활용해서 food[1]부터 food[끝]까지 answer += str(idx) * (food[idx] // 2) 실행
>>> for문 이후, result에 answer + "0" + answer[::-1] 할당 후 return

'''
#===================================================================================

def solution(food):
    answer = ""

    for idx in range(1, len(food)):
        answer += str(idx) * (food[idx] // 2)

    result = answer + "0" + answer[::-1]
    return result


#===================================================================================

food = [1,7,1,2]
print(solution(food)) # "111303111"

# def solution(food):
#     answer = ""
#
#     return answer