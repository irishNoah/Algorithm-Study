# 1260 / DFS와 BFS / S2
# https://www.acmicpc.net/problem/1260

from collections import deque

N, M, V = map(int, input().split())

# 기본적으로 dfs, bfs에서
# 각 노드마다 다른 노드와의 연결 관계가 노드 번호 순서대로 차례로 본인 노드를 제외한 나머지 노드만 명시되어 있다면 이것은 리스트 방식이고, 
# 한 노드가 어느 노드와 연결되어 있다고 그 노드와 다른 노드가 쌍을 이뤄 나와 있다면 이것은 행렬 방식이다.
# 이 문제는 행렬 방식이므로 2차원 행렬을 생성한다.
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M) :
    m1, m2 = map(int, input().split())
    # 노드 연결하기
    # 즉 A,B는 B,A 관계이고 관계가 있는 노드에 대해서는 1이라는 값을 대입
    graph[m1][m2] = graph[m2][m1] = 1

# 깊이 우선 탐색 dfs 구현 함수
def dfs(start_v, discoverd=[]):
    # discoverd = []
    discoverd.append(start_v)
    print(start_v, end=' ')

    for w in range(len(graph[start_v])):
        if graph[start_v][w] == 1 and (w not in discoverd):
            dfs(w, discoverd)

# 너비 우선 탐색 bfs 구현 탐색
def bfs(start_v):
    discoverd = [start_v]
    # 리스트를 써서 pop(0)를 하게 되면 시간복잡도가 O(N)이다.
    # 따라서 시간 복잡도가 O(1)인 deque를 사용해야 한다.
    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in range(len(graph[start_v])):
            if graph[v][w] == 1 and (w not in discoverd):
                discoverd.append(w)
                queue.append(w)

dfs(V)
print()
bfs(V)