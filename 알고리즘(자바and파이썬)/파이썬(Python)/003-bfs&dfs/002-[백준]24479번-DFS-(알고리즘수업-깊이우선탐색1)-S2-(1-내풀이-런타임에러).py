# [백준]24479번-DFS-(알고리즘수업-깊이우선탐색1)-S2-(1-내풀이-런타임에러)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/24479

# 깊이 우선 탐색을 하기 위한 사용자 정의 함수 dfs
def dfs(table, v, visited):
    #현재 노드를 방문처리
    visited[v] = True

    # print(v, end=" ")

    # 방문한 노드를 move에 추가
    move.append(v)

    # dfs 수행
    for i in table[v]:
        if not visited[i]:
            dfs(table, i , visited)

# -------------------------------------------------------

# 정점의 수 n, 간선의 수 m, 시작 정점 r 입력
n, m, r = map(int, input().split())

# 각 정점 순서대로 이어진 정점이 무엇이 있는지에 대한 정보를 담아둘 리스트 table
table = [[] for i in range(m+1)]

for j in range(1, m+1):
    # 간선 정보 a, b 입력
    a, b = map(int, input().split())

    # 각 노드의 정보를 담음
    table[a].append(b)
    table[b].append(a)

# 2차원 리스트 table 배열 정렬
for k in range(m+1):
    table[k] = sorted(table[k]) 


# 방문 했는지에 대한 여부를 파악하는 리스트 visited 생성
visited = [False] * (m+1)

# 방문한 노드를 순서대로 담은 리스트 move 생성
move = []

# 사용자 정의 함수 dfs 수행
dfs(table, 1, visited)

# 아무 노드를 방문하지 않는 정점 수 파악
findLen = m - len(move)

if findLen > 0:
    for _ in range(findLen):
        move.append(0)

# 리스트 move 출력 (= 최종출력)
for t in range(m):
    print(move[t])

'''
vs code 상에서는 올바른 결과를 얻었지만
백준에서는 런타임 에러 판정을 받게 됐다.
'''