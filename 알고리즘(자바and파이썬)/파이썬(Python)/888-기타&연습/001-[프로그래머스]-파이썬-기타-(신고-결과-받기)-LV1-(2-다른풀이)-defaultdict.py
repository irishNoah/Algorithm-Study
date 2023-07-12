# [프로그래머스]-파이썬-기타-(신고-결과-받기)-LV1-(2-다른풀이)-defaultdict.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

'''
*** 참고 URL
https://velog.io/@stella317/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%8B%A0%EA%B3%A0-%EA%B2%B0%EA%B3%BC-%EB%B0%9B%EA%B8%B0Python

*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건(제한사항)

*** 설계 [총 15분 소요] / 총 풀이 시간[총 50분 소요]
>>> 2차원 딕셔너리와 1차원 딕셔너리를 활용한다.

> for문 활용 >> id_list에 들어있는 id를 기준으로 info 딕셔너리의 키로 넣는다.
> 신고 횟수 카운트하는 딕셔너리 cnt 생성
> for문 활용
    > map 활용해 있는 것은 info[report의 앞][report의 뒤] 있는지 check
        > 없으면
            >값 추가
            > cnt[report의 뒤] 값 1로 초기화
        > 있으면
            >cnt[report의 뒤] 값 1 증가

*** 정확성 테스트
- 100점
'''
# #############################################################

from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    # 중복 신고 제거
    report = list(set(report))
    # user별 신고한 id 저장
    user = defaultdict(set) ### defaultdict(타입) >>> keyError를 발생시키지 않는다!
    # user별 신고당한 횟수 저장
    cnt = defaultdict(int)

    for r in report:
        # report의 첫번째 값은 신고자id, 두번째 값은 신고당한 id
        a, b = r.split()
        # 신고자가 신고한 id 추가
        user[a].add(b)
        # 신고당한 id의 신고 횟수 추가
        cnt[b] += 1

    print(user) # defaultdict(<class 'set'>, {'apeach': {'muzi', 'frodo'}, 'frodo': {'neo'}, 'muzi': {'neo', 'frodo'}})
    print(cnt) # defaultdict(<class 'int'>, {'frodo': 2, 'neo': 2, 'muzi': 1})

    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)
    return answer

# =========================================================

# def solution(id_list, report, k):
#     answer = []
#     return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))

# word = "muzi frodo"
# before, after = map(str, word.split())
# print(before, after)