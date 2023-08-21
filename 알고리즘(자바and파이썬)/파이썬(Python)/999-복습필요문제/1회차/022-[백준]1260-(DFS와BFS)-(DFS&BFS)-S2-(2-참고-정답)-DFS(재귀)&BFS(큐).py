# [백준]1260-(DFS와BFS)-(DFS&BFS)-S2-(2-참고-정답)-DFS(재귀)&BFS(큐).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1260

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 5분 소요] / 총 풀이 시간[총 -분 소요]
- 양방향이라고 나와있지만, 어차피 그래프를 각 노드별로 연결 정보를 생성하기 때문에 이게 양방향
- 오름차순, 즉 작은 것부터 차례대로 방문

*** 참고
> https://ji-gwang.tistory.com/291

'''
#===================================================================================
# DFS(그래프-재귀) & BFS(그래프-큐)
from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:

        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

# dfs
visited = [False] * (N + 1)
dfs(V)
print()

# bfs
visited = [False] * (N + 1)
bfs(V)


#===================================================================================