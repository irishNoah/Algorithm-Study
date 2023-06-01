# [프로그래머스]-파이썬-구현(위클리챌린지)-(부족한금액계산하기)-LV1-(2-다른풀이).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/82612

'''
# 느낀점

이 풀이를 좀 더 길게 쓰면 내 풀이와 동일하다
하지만, 동일한 풀이라면 좀 더 간결하게 쓰는 것이 좋을 것이다.
내가 쓰는 for문은 C나 Java에서 보는 for문과 비슷한 형식이다.

하지만, 파이썬에서의 for문은 이 풀이처럼 좀 더 간략히 쓸 수 있다.
앞으로는 좀 더 파이써닉하게 프로그래밍을 할 수 있도록 노력해야겠다.
'''

def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))

price, money, count = map(int, input().split())

print(solution(price, money, count))