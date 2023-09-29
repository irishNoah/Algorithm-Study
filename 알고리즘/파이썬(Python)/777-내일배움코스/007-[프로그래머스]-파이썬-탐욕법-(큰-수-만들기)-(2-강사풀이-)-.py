# [프로그래머스]-파이썬-탐욕법-(큰-수-만들기)-(2-강사풀이-)-.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]
> 주어진 숫자(number)로부터 하나씩 꺼내어 모으되
    - 이 때, 이미 모아둔 것 중 지금 등장한 것보다 작은 것들은 빼낸다.
    - 이것은 어디서 어떻게 살펴보아야?
> 이렇게 모은 숫자들을 자릿수 맞추어 반환한다.
    - 아직 뺄 개수 (k)를 채우지 못한 경우
        - 예를 들어, number가 "98765"이고, k가 "2"일 경우는?
            - 어느 정도 정렬될 경우...
    - 자릿수는 어떻게 계산하는가?

>>> 최종 시간 복잡도는 O(N)

'''
#===================================================================================

def solution(number, k):

    collected = []
    # cnt = 0
    for i, num in enumerate(number):
        # while문 > 기존에 있던 collected의 마지막 값과 num을 비교한다.
        # collected[-1]이 num보다 같거나 끌 때까지 pop을 진행한다.
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        # 만약, append할 것이 남아있어도, k가 0이 됐다면, 더이상 append로 할 필요 없이
        # 남은 것은 collected에 더해주면 된다.
        if k == 0:
            collected += list(number[i:])
            break

        collected.append(num)

    ### k가 남아 있을 경우
    # number가 "98765"이고, k가 2와 같은 경우, 위 for문에서는 해결할 수 없다.
    # 이럴 경우, 위 for문을 통해 생성된 collected에서 남아있는 k개 이전만큼만 추출한다.
    collected = collected[:-k] if k>0 else collected

    answer = ''.join(collected)

    return answer

#===================================================================================

# # 예제 1
# number = "1924"
# k = 2
# print(solution(number, k)) # "94"
#
# # 예제 2
# number = "1231234"
# k = 3
# print(solution(number, k)) # "3234"

# # 예제 3
# number = "4177252841"
# k = 4
# print(solution(number, k)) # "775841"

# 예제 4
number = "98765"
k = 2
print(solution(number, k)) # "987"

# def solution(number, k):
#     answer = ''
#     return answer