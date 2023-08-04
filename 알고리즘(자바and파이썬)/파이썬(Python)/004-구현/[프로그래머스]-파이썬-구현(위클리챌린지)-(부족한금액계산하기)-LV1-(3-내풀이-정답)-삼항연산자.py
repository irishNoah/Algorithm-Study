# [프로그래머스]-파이썬-구현(위클리챌린지)-(부족한금액계산하기)-LV1-(3-내풀이-정답)-삼항연산자.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/82612

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 5분 소요] / 총 풀이 시간[총 10분 소요]


'''
#===================================================================================

def solution(price, money, count):

    check = price * sum(i for i in range(count+1))
    answer = abs(money - check) if 0 > money-check else 0

    return answer

#===================================================================================

# 예제 1
price = 3; money = 20; count = 4
print(solution(price, money, count)) # 10

# def solution(price, money, count):
#     answer = -1
#
#     return answer