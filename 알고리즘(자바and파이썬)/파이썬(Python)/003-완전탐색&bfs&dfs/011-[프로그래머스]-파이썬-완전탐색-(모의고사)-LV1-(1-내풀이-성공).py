# [프로그래머스]-파이썬-완전탐색-(모의고사)-LV1-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

'''
*** 참고 URL

*** 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건(제한사항)
>>> 시험은 최대 10,000 문제로 구성되어있습니다.
>>> 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
>>> 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

>>> 1번 수포자 : 1, 2, 3, 4, 5
>>> 2번 수포자 : 2, 1, 2, 3, 2, 4, 2, 5
>>> 3번 수포자 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5

*** 설계 [총 15분 소요] / 총 풀이 시간[총 40분 소요]
> 수포자 1,2,3이 찍는 번호 목록은 정해져 있는 상황
> 단, answers의 길이가 얼마나 될 지 모른다.
> 따라서, 매칭을 시킬려면 answers[i]일 때 각 수포자1,2,3[i % len(수포자1,2,3)] 을 비교해서
    > 맞으면 정답값 1 증가


*** 정확성 테스트
- 100점
'''
# #############################################################

def solution(answers):
    answer = []

    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt1 = 0; cnt2 = 0; cnt3 =0
    for i in range(len(answers)):
        if person1[i % len(person1)] == answers[i]:
            cnt1 += 1
        if person2[i % len(person2)] == answers[i]:
            cnt2 += 1
        if person3[i % len(person3)] == answers[i]:
            cnt3 += 1

    print(cnt1, cnt2, cnt3)
    check = max(cnt1, cnt2, cnt3)
    print(check)

    if check == cnt1:
        answer.append(1)
    if check == cnt2:
        answer.append(2)
    if check == cnt3:
        answer.append(3)

    return answer

# =========================================================

answers = [1,3,2,4,2]
print(solution(answers))