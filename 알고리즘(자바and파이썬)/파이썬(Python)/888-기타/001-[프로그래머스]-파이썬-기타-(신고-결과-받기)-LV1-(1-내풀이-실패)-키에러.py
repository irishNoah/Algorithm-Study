# [프로그래머스]-파이썬-기타-(신고-결과-받기)-LV1-(1-내풀이-실패)-키에러.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

'''
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

import sys

def solution(id_list, report, k): # 아이디 목록, 신고 현황, 정지 기준 횟수
    answer = []

    info = dict()
    for val in id_list:
        info[val] = dict()

    # 신고 현황 파악
    cnt = dict()
    for word in report:
        before, after = map(str, word.split())

        if info[before].get(after) == None:
            info[before][after] = 1
            cnt[after] = 1

        if info[before].get(after) != None:
            cnt[after] += 1



    # 신고 처리 결과 메일
    mail = dict()
    list_key = cnt.keys()
    print(list_key)

    for idx in list_key:
        print(cnt[idx])
        if cnt[idx] >= k : # 정지 기준 횟수 이상이 되면
            for cmp in range(len(info)): # info를 뒤져
                # =========================================
                # keyError : 0 발생
                if info[cmp].get(idx) != None: # info[cmp]에 idx 키가 있으면
                    print("HELLO")
                    if mail.get(idx) == None:
                        mail[idx] = 1
                    else:
                        mail[idx] += 1

    return mail

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