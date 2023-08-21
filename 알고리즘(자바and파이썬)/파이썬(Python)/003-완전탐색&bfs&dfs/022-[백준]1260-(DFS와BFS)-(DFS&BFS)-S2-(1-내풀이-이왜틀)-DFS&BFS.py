# [백준]1260-(DFS와BFS)-(DFS&BFS)-S2-(1-내풀이-이왜틀)-DFS&BFS.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1260

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 5분 소요] / 총 풀이 시간[총 -분 소요]
- 양방향이라고 나와있지만, 어차피 그래프를 각 노드별로 연결 정보를 생성하기 때문에 이게 양방향
- 오름차순, 즉 작은 것부터 차례대로 방문

*** 참고
> https://hongcoding.tistory.com/71

'''
#===================================================================================
# DFS(그래프-스택) & BFS(그래프-큐)
import sys
from collections import deque # BFS 큐 사용 위해
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfsGraph = graph # dfs용 그래프
bfsGraph = graph # bfs용 그래프

# dfsGraph 내림차순 정렬 (오름차순 정렬해도 똑같음)
for idx in range(1, N+1):
    dfsGraph[idx].sort()

# bfsGraph는 오름차순 정렬
for idx in range(1, N+1):
    bfsGraph[idx].sort()

visitedDfs = [-1] * (N+1)
resultDfs = [] # DFS 방문 노드 순서 결과 리스트
def dfs(start):

    stack = [start]

    while stack:
        # print("stack = ", stack)
        top = stack.pop()

        if visitedDfs[top] == 1:
            continue

        visitedDfs[top] = 1
        resultDfs.append(top) # 방문 노드를 결과 리스트에 할당

        for adjNode in dfsGraph[top]:
            if visitedDfs[adjNode] == -1:
                # print("11111")
                stack.append(adjNode)
                break # continue가 아닌 break로 해야 한다!!!

    return resultDfs

visitedBfs = [-1] * (N+1)
resultBfs = [] # BFS 방문 노드 순서 결과 리스트
def bfs(start):

    queue = deque([start])

    while queue:
        node = queue.popleft()

        if visitedBfs[node] == 1:
            continue

        visitedBfs[node] = 1
        resultBfs.append(node)

        for adjNode in bfsGraph[node]:
            if visitedBfs[adjNode] == -1:
                queue.append(adjNode)

    return resultBfs

print(*dfs(R))
print(*bfs(R))


#===================================================================================