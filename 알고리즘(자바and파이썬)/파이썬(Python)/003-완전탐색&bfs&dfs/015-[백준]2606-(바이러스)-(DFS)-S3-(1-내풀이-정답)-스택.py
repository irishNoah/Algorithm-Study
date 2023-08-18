# [백준]2606-(바이러스)-(DFS)-S3-(1-내풀이-정답)-스택.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2606

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 6분 소요] / 총 풀이 시간[총 15분 소요]

*** 참고

'''
#===================================================================================

import sys
input = sys.stdin.readline

com = int(input().rstrip()) # 컴퓨터의 수
line = int(input().rstrip()) # 연결된 컴퓨터 쌍의 수

graph = [[] for _ in range(com+1)] # 각 컴퓨터마다 연결된 정보
for _ in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 그래프 내림차순 정렬 >>> 그래야 stack에서 오름차순 정렬로 접근하니까
for idx in range(1, len(graph)):
    graph[idx].sort(reverse=True)

visited = [-1] * (com+1) # 방문 여부

# DFS 알고리즘 활용하여 웜 바이러스 개수 세기
def dfs(start):
    stack = [start]
    cnt = -1 # 감염된 컴퓨터의 수(단, 1번 컴퓨터는 제외시켜야 줘야 해서 -1로 설정)

    while stack:
        top = stack.pop()

        ### 이전에 방문한 적 있으면 다음꺼 진행
        if visited[top] == 1:
            continue

        ### 이전에 방문한 적이 없다면
        visited[top] = 1 # 방문한 것으로 변경
        cnt += 1 # 감염 컴퓨터 수 증가

        # 해당 노드의 하위 노드 중에 아직 방문한 적이 없는
        # 노드가 잇다면 스택에 추가
        for adjNode in graph[top]:
            if visited[adjNode] == -1:
                stack.append(adjNode)

    return cnt

print(dfs(1)) # 1번부터 감염된다고 지문에 나옴



#===================================================================================