# [프로그래머스]-파이썬-힙-(기말고사)-(2-강사풀이-이해가안감)-힙활용.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
1) 일단은 study, pstudy에서 가장 적은 cost인것을 t가 넘어갈 때까지 계속 더해주면 된다.
이것이 문제가 되는 경우는 두가지인데
    a. 하나는 pstudy에서 뽑은것이 k개가 넘어갈때이고
    b. 두번째는 study에서 뽑은 것과 pstudy에서 뽑은것이 겹칠때이다.

2) a의 경우 diff라는 heapq를 사용하여 해결할 수 있다.
diff에는 k개의 0으로 초기화되어있으며 (처음 k개는 아무 페널티없이 pstudy에서 뽑을 수 있으므로),
만약에 pstudy에서 어떠한 과목을 뽑았다면 diff에 study와의 차이값을 넣어준다.
이렇게 pstudy에서 뽑은 과목이 k개가 된 경우,
그 다음에 또 pstudy에서 어떤 과목을 뽑게 된다면 diff가 가장 작은 과목을 pstudy -> study로 바꾸면서까지
뽑을 가치가 있는 것인지 판단을 하게 된다.
(diff[0] + paper_hq[pidx][0] < study_hq[sidx][0]) 그러할 가치가 없는 경우 pstudy 대신 study에서 뽑으면 된다.

3) b의 경우 visited를 두어 겹치지 않도록 체크를 할 수 있다.

*** 참고

'''
#===================================================================================
from heapq import heappush, heappop, heapify


def solution(t, k, study, pstudy):
    print("=" * 50)
    visited = [0] * len(study)
    diff = [0] * k
    print("set visited = ", visited) # 예제 1 > [0, 0, 0, 0, 0]
    print("set diff", diff) # 예제 1 > [0, 0]

    # 값을 기준으로 오름차순 정렬하되, 값이 동일할 경우 인덱스 기준으로 오름차순 정렬
    study_hq = [(s, i) for i, s in enumerate(study)]
    paper_hq = [(p, i) for i, p in enumerate(pstudy)]
    study_hq.sort()
    paper_hq.sort()

    # print("sort study_hq", study_hq) # 예제 1 > [(5, 4), (8, 0), (8, 2), (9, 3), (13, 1)]
    # print("sort paper_hq", paper_hq) # 예제 1 > [(1, 0), (3, 1), (4, 2), (4, 4), (7, 3)]

    sidx, pidx = 0, 0

    while sidx < len(study):

        if diff[0] + paper_hq[pidx][0] < study_hq[sidx][0]:
            c, i = paper_hq[pidx]
            # print("c = ", c, " i = ", i)
            c += diff[0]
            heappop(diff)
            heappush(diff, study[i] - pstudy[i])
        else:
            c, i = study_hq[sidx]

        # print("while diff = ", diff)

        if c > t:
            break

        t -= c
        visited[i] = 1

        while sidx < len(study) and visited[study_hq[sidx][1]]:
            sidx += 1
        while pidx < len(study) and visited[paper_hq[pidx][1]]:
            pidx += 1

        # print("while visited = ", visited)

    print()

    return sum(visited)

#===================================================================================

# 예제 1
t = 10
k = 2
study = [8,13,8,9,5]
pstudy = [1,3,4,7,4]
print(solution(t, k, study, pstudy)) # 3

# 예제 2
t = 100
k = 3
study = [90,100,90,80,40,50]
pstudy = [1,2,3,10,20,30]
print(solution(t, k, study, pstudy)) # 4

# def solution(t, k, study, pstudy):
#     answer = 0
#     return answer