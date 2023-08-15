# [백준]24479-(알고리즘 수업 - 깊이 우선 탐색 1)-(DFS)-S2-(2-참고풀이-)-재귀.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/24479

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
-

*** 참고
- zip() >>> https://www.daleseo.com/python-zip/

'''
#===================================================================================

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
path = []
result = [0] * (N + 1)
visited = [-1] * (N + 1)

print("set graph = ", graph) # set graph =  [[], [], [], [], [], []]
print("set result = ", result) # set result =  [0, 0, 0, 0, 0, 0]
print("set visited = ", visited) # set visited =  [-1, -1, -1, -1, -1, -1]

### 자신의 노드와 닿는 모든 인접 노드를 할당한다.
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 재귀에서는 차례대로 접근하기 위해 오름차순 정렬 <-> 스택에서는 차례대로 접근하기 위해서는 내림차순 정렬 
for i in range(1, len(graph)):
    graph[i].sort()

print("sort graph = ", graph) # sort graph =  [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]

def DFS(start):
    visited[start] = 1
    path.append(start)

    for adj_node in graph[start]:
        if visited[adj_node] == -1:
            DFS(adj_node)

    return


DFS(R) ### 이거를 해줘야 방문순서를 알 수 있음
print("status of visited[] after DFS(R) = ", visited) # status of visited[] after DFS(R) =  [-1, 1, 1, 1, 1, -1]
print("status of path[] after DFS(R) = ", path) # status of path[] after DFS(R) =  [1, 2, 3, 4]

for idx, node in zip(range(1, len(path) + 1), path):
    print("idx =  ", idx, "node = ", node)
    # zip()을 통해서 데이터를 묶어주고, 결과값을 순서대로 할당
    result[node] = idx
    print("result[node] = ", result[node])

print("*result[1:] = ", *result[1:], sep="\n")

#===================================================================================