# [프로그래머스]-파이썬-기타-(신고-결과-받기)-LV1-(3-내풀이-정답)-defaultdict활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

'''
*** 참고 URL

*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건(제한사항)

*** 설계 [총 15분 소요] / 총 풀이 시간[총 35분 소요]
- report를 set()해서 중복되는 신고를 없앤다.
- defaultdict를 활용해서 report에 있는 것을 공백 구분하여 dict화 한다.
    - 앞에 있는 것은 키, 뒤에 있는 것은 값 >>> (infor)
        - 값에 해당하는 딕셔너리(cntReport)를 활용해서 신고 횟수를 카운트한다.
- 결과 메일(mail / 딕셔너리) >>> int: 0 for int in id_list}
- cntReport의 키의 값이 k 이상인 것(=조건)과, cntReport 각 키 값 중에서 조건과 일치한 것이 있다면
infor과 비교해서 mail에 1 추가

*** 정확성 테스트
- 100점
- 테스트가 24개가 있는데 나머지는 전반적으로 좋았지만
    - 테스트 3 : 통과 (3373.18ms, 39.3MB)
    - 테스트 9 : 통과 (804.45ms, 23.8MB)
    - 테스트 10 : 통과 (72.44ms, 23.8MB)
    - 테스트 11 : 통과 (2019.03ms, 39.3MB)
    - 테스트 14 : 통과 (1087.05ms, 22.5MB)
    - 테스트 15 : 통과 (118.91ms, 32.5MB)
    - 테스트 20 : 통과 (934.51ms, 22.6MB)
    - 테스트 21 : 통과 (2617.61ms, 32.5MB)

이건 고쳐봐야 겠다.

'''
# #############################################################

import sys
from collections import defaultdict

def solution(id_list, report, k):

    report = list(set(report))

    infor = defaultdict(list)  # 각 사람이 누구를 신고했는지 알 수 있는 정보
    cntReport = defaultdict(int)  # 특정인이 몇 번 신고를 당했는지 알 수 있는 정보
    for inf in report:
        singo, pihae = inf.split(" ")

        infor[singo].append(pihae)
        cntReport[pihae] += 1

    mail = {int: 0 for int in id_list}  # 결과 메일 횟수 세기

    for val in cntReport:  # 신고 당한 횟수 중에서
        if cntReport[val] >= k:  # 계정 정지 횟수에 부합한 사람이 있을 경우
            for cmp in infor:  # 각 사람의 신고 목록 중에서
                if val in infor[cmp]:  # 신고 당한 사람이 있을 경우
                    mail[cmp] += 1  # 결과 메일 값을 한 개 증가

    return list(mail.values())

# =========================================================

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k)) # [2, 1, 1, 0]