# [프로그래머스]-파이썬-구현-(콜라-문제)-LV1-(2-참고)-정답.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/132267


def solution(a, b, n):
    answer = 0
    # 단, 보유 중인 빈 병이 2개 미만이면, 콜라를 받을 수 없다.
    # 빈 병의 개수가 콜라를 받기 위해서 필요한 개수보다 크면 반복한다
    while (n >= a):
        remain_bottle = n % a
        n = (n//a) * b # 마트에서 받은 콜라의 수
        answer += n # 받은 걸 answer에 +
        n += remain_bottle # 남아있는 병을 더해줘서 다음에 마트갈 때 이용
    return answer