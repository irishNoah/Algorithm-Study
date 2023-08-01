# [프로그래머스]-파이썬-중간고사2번-그리디-(티셔츠)-(2-강사풀이-성공)-투포인터.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
작은 사람부터 작은 옷부터 입히면 가장 효율적입니다.
즉, 정렬 후 tshirts을 하나씩 살펴보면서 people보다 크면 입히고, 아니면 넘기면 됩니다.
구현은 이전 문제와 같이 투포인터를 활용하면 됩니다.

*** 참고

'''
#===================================================================================

def solution(people, tshirts):
    people.sort()
    tshirts.sort()

    p, t, ans = 0, 0, 0

    # 투 포인터를 활용해서 푼다!
    # 가급적 while True보다는 이렇게 풀기
    while p < len(people) and t < len(tshirts):
        if tshirts[t] >= people[p]:
            ans += 1
            p += 1
        t += 1

    return ans

#===================================================================================

# 예제 1
people = [2, 3]
tshirts = [1, 2, 3]
print(solution(people, tshirts)) # 2

# 예제 2
people = [1, 2, 3]
tshirts = [1, 1]
print(solution(people, tshirts)) # 1

# def solution(people, tshirts):
#     answer = 0
#     return answer