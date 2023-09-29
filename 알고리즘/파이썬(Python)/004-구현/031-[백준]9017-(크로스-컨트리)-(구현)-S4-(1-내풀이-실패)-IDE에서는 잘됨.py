# [백준]9017-(크로스-컨트리)-(구현)-S4-(1-내풀이-실패)-IDE에서는 잘됨.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/9017

'''
*** 제한 > 시간 : 1초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건
- 데이터 개수 : 1000 (따라서 O(N^3))

*** 설계 [총 27분 소요] / 총 풀이 시간[총 67분 소요]

*** 참고

'''
#===================================================================================
import sys
input = sys.stdin.readline

case = int(input().rstrip()) # 테스트 케이스 개수

while case > 0:
    case -= 1 # while문 탈출 조건

    data = int(input().rstrip()) # 주자 인원수
    point = list(map(int, input().split())) # 각 팀의 주자가 들어온 순서 담은 리스트

    # print("point =", point)

    team = [] # 팀이 6명으로 구성되어 있는지 파악하는 리스트
    val = max(point) # 팀의 갯수 파악
    for idx in range(1, val+1):
        if point.count(idx) == 6:
            team.append(idx)

    # print("team =", team)

    rank = dict() # 팀이 6명으로 구성된 팀의 주자들의 점수를 담은 딕셔너리
    ### 팀 번호를 키로 활용, 리스트를 값으로 활용
    for idx in team:
        rank[idx] = list()

    cnt = 0 # 각 주자의 점수
    ### 각 팀 주자의 점수를 딕셔너리에 할당
    for i in range(len(point)):
        if point[i] in rank:
            cnt += 1
            rank[point[i]].append(cnt)

    # print("rank = ", rank)

    sumRun = [] # 아래 정보를 담는 2차원 리스트
    ### 각 팀의 팀번호, 상위 4등까지 점수 합산, 5등의 점수를 sumRun에 할당
    for key in rank.keys():
        infor = [key, sum(rank[key][:4]), rank[key][4]]
        sumRun.append(infor)

    # print("sumRun = ", sumRun)

    ### sumRun의 길이가 1이면, 해당 팀 번호 출력
    if len(sumRun) == 1:
        print(sumRun[0][0])

    ### sumRun의 길이가 1보다 크면, 5번째 선수 비교하여 출력
    else:
        winner = -1
        cmp = 999
        ### 5번째 선수 중 가장 낮은 등수 체크
        for idx in range(len(sumRun)):
            if sumRun[idx][2] <= cmp:
                cmp = sumRun[idx][2]
                # winner = sumRun[idx][0]

        ### 가장 낮은 등수를 받은 5번째 선수가 여러명일 수 있음
        result = []
        for idx in range(len(sumRun)):
            if sumRun[idx][2] == cmp:
                result.append(sumRun[idx][0])

        print(*result) # 결과 출력

#===================================================================================