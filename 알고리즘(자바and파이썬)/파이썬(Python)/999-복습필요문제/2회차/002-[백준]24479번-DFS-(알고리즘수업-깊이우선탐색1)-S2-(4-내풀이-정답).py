# [백준]24479번-DFS-(알고리즘수업-깊이우선탐색1)-S2-(4-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/24479

### 스택 활용해 dfs 구성
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

# 그래프 생성 >>> 각 노드마다 연결된 정보 파악하기 위해
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 그래프의 각 노드에 대한 연결 정보 내림차순 정렬 >>> 그래야 나중에 pop()을 활용하니깐!
for idx in range(1, len(graph)):
    graph[idx].sort(reverse=True)

visited = [-1] * (N+1) # 방문 여부 확인
path = [0] * (N+1) # 각 노드가 방문된 순서

def dfs(start): # 스택으로 dfs 구성
    # print(1)
    stack = [start]
    cnt = 1 # 방문 순서

    while stack:
        node = stack.pop() # 최상위 원소

        # 이미 방문된 최상단 노드라면 continue
        if visited[node] == 1:
            continue

        # 방문이 아직 안 된 상태라면
        visited[node] = 1 # 방문 처리
        path[node] = cnt  # 방문 순서 할당
        cnt += 1

        # 해당 노드에 존재하는 하위 노드를 stack에 할당
        for adNode in graph[node]:
            if visited[adNode] == -1:
                stack.append(adNode)

    return path

dfs(R)

print(*path[1:], sep='\n')