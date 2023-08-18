# [백준]24480-(알고리즘 수업 - 깊이 우선 탐색 2)-(DFS)-S2-(1-내풀이-정답)-스택.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/24480

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 3분 소요] / 총 풀이 시간[총 9분 소요]

*** 참고

'''
#===================================================================================

import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

# 그래프에서 각 노드마다 연결된 노드 정보 파악
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

# 각 그래프의 노드마다 오름차순 정렬 >>> 그래야 스택에서 내림차순으로 pop() 가능
for idx in range(1, len(graph)):
    graph[idx].sort()

visited = [-1] * (N+1) # 각 노드의 방문 여부
result = [0] * (N+1) # 각 노드의 방문된 순서

def dfs(start):
    stack = [start]
    cnt = 1 # 방문 순서

    while stack:
        top = stack.pop() # 최상위 원소

        if visited[top] == 1: # 방문된 적 있으면 지나감
            continue

        # 없으면???
        visited[top] = 1 # 방문 처리
        result[top] = cnt # 해당 노드의 방문 순서 할당
        cnt += 1

        # 해당 노드의 하위 노드 중 아직 방문하지 않은 노드를 스택에 할당
        for adjNode in graph[top]:
            if visited[adjNode] == -1:
                stack.append(adjNode)

    return result

dfs(R)
print(*result[1:], sep='\n')




#===================================================================================