# [백준]24444-(너비우선탐색1)-(DFS&BFS)-S2-(1-내풀이-정답)-BFS&큐.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/24444

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- N, M, R 입력
- graph 생성
- graph의 각 노드 기준으로 오름차순 정렬
- 데크 라이브러리를 활용하여 큐 구현
    - while문
        - 큐의 최상단 노드 방문 처리
            - 최상단 노드의 인접 노드 중에서 아직 방문안한 노드 큐 뒤에 할당
            - 최상단 노드 삭제 >>> 방문 순서 cnt 할당

*** 참고
- https://anggeum.tistory.com/entry/24444-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%88%98%EC%97%85-%EB%84%88%EB%B9%84-%EC%9A%B0%EC%84%A0-%ED%83%90%EC%83%89-1-%EC%A0%95%EC%A0%90-%EB%B0%A9%EB%AC%B8-%EC%88%9C%EC%84%9C-%EA%B5%AC%ED%98%84

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

# 각 노드 오름차순 정렬
for idx in range(1, N+1):
    graph[idx].sort()

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