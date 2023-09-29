# [프로그래머스]-파이썬-BFS&DFS-(타켓-넘버)-LV2-(1-내풀이-실패)-정확성37.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건
> 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
> 각 숫자는 1 이상 50 이하인 자연수입니다.
> 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

*** 설계 [총 15분 소요] / 총 풀이 시간[총 35분 소요]
>>> combinations 활용
1. combinations에서 len(numbers)보다 1 작은 것부터 시작해서 -1 씩 한다. (접근은 cmp)
    - 만약, 조합으로 구해진 값의 합이 target 보다 작으면 pass 한다.
    - 만약, 조합으로 구해진 값의 합이 target 보다 크면?
        - abs(sum(numbers) - sum(cmp)*2) == target 인지 확인
            - 다르면 pass
            - 같다면, cmp가 live 리스트에 있는지 확인
                - 없다면 live에 추가 && answer 값 1 증가
                - 있다면 pass

*** 정확성 테스트
- MB는 대부분 10MB
- ms에서 성능 차이가 심하게 남
- 총 37.5점

*** 왜 틀렸을까?
- BFS 및 DFS로 풀어야 효율성에서 좋다.
- 난 이게 아니라, 그냥 for문으로 풀어서 효율성이 안 좋은 것 같다.
- 근데 아직 난 BFS/DFS를 하기는 아직 벅....찬뎅 ㅠㅠ
>>> 다음에 풀 때는 이 URL를 참고해서 풀어보도록 하자.
- https://daeun-computer-uneasy.tistory.com/69

'''
# #############################################################

from itertools import combinations

def solution(numbers, target):
    answer = 0

    leng = len(numbers)

    while True:
        leng = leng - 1

        if leng == 0:
            break

        for cmp in combinations(numbers, leng):
            cmp = list(cmp)

            if sum(cmp) > target:

                if abs(sum(numbers) - sum(cmp)*2) == target:
                    answer += 1

    return answer


# =========================================================

numbers = [4, 1, 2, 1]
target = 4

print(solution(numbers, target))