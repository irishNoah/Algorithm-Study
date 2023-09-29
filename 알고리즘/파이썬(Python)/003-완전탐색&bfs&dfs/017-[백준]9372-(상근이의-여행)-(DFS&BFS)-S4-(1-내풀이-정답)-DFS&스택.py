# [백준]9372-(상근이의-여행)-(DFS&BFS)-S4-(1-내풀이-정답)-DFS&스택.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/9372

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- 주어지는 비행 스케줄은 항상 연결 그래프를 이루기 때문에, 그패프가 끊어질 일은 없다.

*** 참고

'''
#===================================================================================
# DFS & 스택 활용
import sys
input = sys.stdin.readline

case = int(input().rstrip()) # 테스트 케이스 출력

while case > 0:
    case -= 1

    N, M = map(int, input().split()) # 국가의 수 / 비행기의 종류 입력

    graph = [[] for _ in range(N+1)]
    visited = [-1] * (N+1) # 방문 여부
    for _ in range(M):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    # 그래프 > 각 노드마다 내림차순 정렬 for 스택의 pop()
    for idx in range(1, len(graph)):
        graph[idx].sort(reverse=True)

    count = -1 # 사용해야 하는 비행기의 수(단, 노드 중점 탐색이므로 1번 노드 값은 제외해줘야 함)
    def dfs(start):  # 1번부터 시작한다고 가정한다.
        global count

        stack = [start]

        while stack:
            top = stack.pop()

            ### 이미 방문했거나, 순회 구조라면 continue
            if visited[top] == 1:
                continue

            ### 그렇지 않다면~
            visited[top] = 1 # 방문 처리
            count += 1 # 이용 비행기 수 1 증가

            # 아직 해당 탑노드에서 방문하지 않은 노드가 있다면 스택에 할당
            for adjNode in graph[top]:
                if visited[adjNode] == -1:
                    stack.append(adjNode)

        return count

    print(dfs(1))

#===================================================================================