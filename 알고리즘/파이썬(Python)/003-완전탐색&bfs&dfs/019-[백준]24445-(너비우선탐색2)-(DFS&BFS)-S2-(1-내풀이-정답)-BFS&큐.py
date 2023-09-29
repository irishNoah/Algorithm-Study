# [백준]24445-(너비우선탐색2)-(DFS&BFS)-S2-(1-내풀이-정답)-BFS&큐.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/24445

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- 인접 노드는 내림차순으로 진행한다.

*** 참고

'''
#===================================================================================
# BFS & 큐(데크 라이브러리) 활용
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)] # 각 노드의 연결 정보
visited = [-1] * (N+1) # 각 노드의 방문 여부
result = [0] * (N+1) # 각 노드의 방문 순서 리스트

# 각 노드 연결 정보 할당
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드 내림차순 정렬
for idx in range(1, N+1):
    graph[idx].sort(reverse=True)

def bfs(start):
    queue = deque([start])
    cnt = 1 # 각 노드의 방문 순서
    visited[start] = 1
    result[start] = cnt
    cnt += 1

    while queue:
        node = queue.popleft()

        for adjNode in graph[node]:
            if visited[adjNode] == -1:
                queue.append(adjNode)
                visited[adjNode] = 1
                result[adjNode] = cnt
                cnt += 1

bfs(R) # R번 노드부터 시작

print(*result[1:], sep='\n')


#===================================================================================