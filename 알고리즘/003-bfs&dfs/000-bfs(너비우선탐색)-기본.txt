# bfs(너비우선탐색)-기본
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v=queue.popleft() # 노드 v에 queue의 맨 첫 번째 요소 할당
        print(v,end=' ') # v 출력

        # graph[v] 탐방 > 만약, v가 3이라면 graph[v]는 [1,4,5]
        for i in graph[v]: 
            # graph[v] 중에서 visited[i]가 false인 경우 아래 if문 수행
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 그래프 정보
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9

print(visited)

bfs(graph,1,visited)