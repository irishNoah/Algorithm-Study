# [백준]1260-(DFS와BFS)-(DFS&BFS)-S2-(3-내풀이-정답)-DFS(재귀)&BFS(큐)-방문여부를언제변경해주냐가관건.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1260

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 5분 소요] / 총 풀이 시간[총 -분 소요]
- 양방향? >>> DFS(재귀) / BFS(큐)
- 여러개 방문할 수 있는 상황에서는 오름차순으로 접근
- visited 리스트를 방문 여부용으로 활용한다. >>> True 또는 False
- 결과 리스트로 result를 활용한다 >>> 여기에 방문된 순서대로 노드를 할당
- dfs든 bfs든 어느 시점에 방문 여부를 False에서 True로 바꾸어줄지가 중요하다.

*** 참고
> https://ji-gwang.tistory.com/291

'''
#===================================================================================
### DFS(그래프-재귀) & BFS(그래프-큐)
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for idx in range(1, N+1):
    graph[idx].sort()

def dfs(start): ### dfs >>> 재귀로 구현
    # 여기서 방문 여부 체크
    visited[start] = True
    print(start, end=" ")

    # 재귀 상황
    for adjNode in graph[start]:
        if visited[adjNode] == False:
            dfs(adjNode)



def bfs(start): ### bfs >>> 큐로 구현
    print()

    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        cmp = queue.popleft()
        print(cmp, end=" ")

        for adjNode in graph[cmp]:
            if visited[adjNode] == False:
                # 여기서 방문 여부 변환
                visited[adjNode] = True
                queue.append(adjNode) # 큐에 추가



### dfs 실행
visited = [False] * (N+1)
dfs(R)

### bfs 실행
visited = [False] * (N+1)
bfs(R)

#===================================================================================