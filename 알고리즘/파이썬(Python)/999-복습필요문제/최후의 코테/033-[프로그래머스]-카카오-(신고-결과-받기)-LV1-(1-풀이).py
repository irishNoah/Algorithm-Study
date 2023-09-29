'''
033-[프로그래머스]-카카오-(신고-결과-받기)-LV1-(1-풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/92334

### 참고
> 없음

17:50~18:26
### 설계 10분, 총 36분
1. id_list 기준
> user = dict()
> user에 id_list를 키로 / 리스트를 값으로 구성한다.
2. report 기준
> 각 report의 요소를 arr이라 가정
> pA, pB = arr.split() # pA는 신고한 사람, pB는 신고받은 사람
> user[pA].append(pB) >>> 신고한 사람 기준으로 신고받은 사람을 다 추가한다
3. 구해진 user 기준으로
> 각 user[신고자]를 set화 해서 신고받은 사람의 중복을 제거한다.
4. cnt_report = dict() >>> 각 유저마다 몇 번 신고당했는지 구하기
> cnt_report에 id_list를 키로 / 숫자 0를 기본값으로 구성한다.
> for문 --- 각 user의 값을 리스트에 담는다. (val)
    - val[0]부터 val[len(val)-1]까지
        - 신고당한 횟수 카운드
5. 구해진 cnt_report를 기준으로 정지된 ID 횟수 체크
> answer = dict() >>> 각 유저마다 신고한 사람 중에 k 이상 신고당해서 알림을 받을 횟수 구하기
    - answer에 id_list를 키로 / 숫자 0를 기본값으로 구성한다.
    - for로 user을 돌아
        - 각 유저의 값을 리스트에 담아
            - 이 리스트에서 cnt_report[유저의 값] >= k 일 경우
                - naswer[유저] += 1

'''


def solution(id_list, report, k):
    answer=0
    
    # step1
    user = dict()
    for id in id_list:
        if user.get(id) == None:
            user[id] = list()
            
    # step2
    for arr in report:
        pA, pB = arr.split()
        user[pA].append(pB)

    # step3
    for pA in user.keys():
        user[pA] = set(user[pA])

    # step4
    cnt_report = dict()
    for id in id_list:
        if cnt_report.get(id) == None:
            cnt_report[id] = 0
    for u in user.keys():
        arr = user[u]
        
        for rpt in arr:
            cnt_report[rpt] += 1
    
    # step5
    answer = dict()
    for id in id_list:
        if answer.get(id) == None:
            answer[id] = 0

    for u in user.keys():
        arr = user[u]

        for val in arr:
            if cnt_report[val] >= k:
                answer[u] += 1
    
    # print(answer)
    code = []
    for key, v in answer.items():
        code.append(v)
    # print(code)
    return code


