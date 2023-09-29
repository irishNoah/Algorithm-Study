# [백준]24479-(알고리즘 수업 - 깊이 우선 탐색 1)-(DFS)-S2-(4-참고-)-스택.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/24479

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 10분 소요] / 총 풀이 시간[총 34분 소요]
>>> 재귀는 근데, 시간 초과라고 뜨는뎅...???

*** 참고

'''
#===================================================================================

import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 내림차순인 인접 그래프를 스택에 하나씩 넣어주면, 나중에 스택에서
# 꺼낼때는 이들을 오름차순으로 꺼내게 됨
for i in range(1, len(graph)):
    graph[i].sort(reverse=True)

visited = [-1] * (N + 1)
result = [0] * (N + 1)  # result[idx]는 idx노드를 방문한 순서 값을 의미함

def DFS(start):
    stack = [start]
    # visited = [-1] * (N + 1)
    # result = [0] * (N + 1)  # result[idx]는 idx노드를 방문한 순서 값을 의미함
    cnt = 1  # 방문 순서 값

    while stack:
        cnt_node = stack.pop()

        # 사이클이 있는 그래프 같은 경우에,
        # 어떤 노드에 대해, 그 노드의 인접 노드 K를 스택에 넣어
        # 놓은 뒤에, DFS를 수행하다가 더 깊은 깊이의 어느 노드에서
        # 인접 노드로 K를 또 스택에 넣는 경우가 생김.
        # 이 때의 K가 먼저 스택에서 꺼내져 처리되므로,
        # 맨 첨 넣어줬던 K는 스택에서 꺼낸 뒤 따로 코드를
        # 수행해주지 않고 넘어감
        if visited[cnt_node] == 1:
            continue

        visited[cnt_node] = 1

        # 방문 순서 값 저장
        result[cnt_node] = cnt
        cnt += 1

        # 아직 방문 이력 없으면(=스택에서 뽑은 적 없으면)
        # 스택에 싹 다 집어 넣기
        for adj_node in graph[cnt_node]:
            if visited[adj_node] == -1:
                stack.append(adj_node)

    return result


result = DFS(R)

print(*result[1:], sep="\n")


#===================================================================================