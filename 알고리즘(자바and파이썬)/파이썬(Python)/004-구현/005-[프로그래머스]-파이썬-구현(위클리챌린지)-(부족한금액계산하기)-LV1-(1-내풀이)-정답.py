# [프로그래머스]-파이썬-구현(위클리챌린지)-(부족한금액계산하기)-LV1-(1-내풀이)-정답.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/82612

'''

'''

def solution(price, money, count):

    sum = 0

    for i in range(1, count+1):
        sum += i

    result = money - price * sum

    if result < 0:
        answer = abs(result)
    else:
        answer = 0

    return answer

price, money, count = map(int, input().split())

print(solution(price, money, count))