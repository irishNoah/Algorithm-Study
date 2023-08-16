# [백준]24479-(알고리즘 수업 - 깊이 우선 탐색 1)-(DFS)-S2-(3-내풀이-정잡)-재귀.py
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
sys.setrecursionlimit(10 ** 9)

N, M, R = map(int, input().split()) # 차례대로 정점의 수 / 간선의 수 / 시작 정점

res = [0] * (N+1) # 결과 리스트
vis = [-1] * (M+1) # 방문 여부 확인 리스트
graph = [[] for _ in range(N+1)] # 각 노드 간 연결 정보를 담은 2차원 리스트
move = [] # 방문 순서 리스트

for _ in range(M): # 간선 정보 받아서 graph에 할당
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)): # 각 노드의 연결 정보를 오름차순 정렬
    graph[i].sort()
print(graph)

def dfs(start): # dfs 구현

    vis[start] = 1      # 방문하지 않는 노드 방문 처리
    move.append(start)  # 방문 순서 리스트 할당

    # 해당 노드의 인접 노드 중 아직 방문하지 않은 곳부터 재귀하여 탐색
    for adNode in graph[start]:
        if vis[adNode] == -1:
            dfs(adNode)

    return

dfs(2) # 시작 정점부터 재귀 시작

# print("move = ", move)

# 결과 리스트에 차례대로 각 노드마다의 방문 순서가 move에서 몇 번째인지 할당
for idx, node in zip(range(1, len(move)+1), move):
    # print("node = ", node, " idx = ", idx)
    res[node] = idx
# print("res = ", res)

# 결과 출력
print(*res[1:], sep='\n')


#===================================================================================