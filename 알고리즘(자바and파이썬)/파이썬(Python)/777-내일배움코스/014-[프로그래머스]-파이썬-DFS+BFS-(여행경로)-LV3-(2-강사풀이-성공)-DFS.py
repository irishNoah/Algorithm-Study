# [프로그래머스]-파이썬-DFS+BFS-(여행경로)-LV3-(2-강사풀이-성공)-DFS.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- 스택을 이용한 재귀 알고리즘 DFS 활용

*** 참고

'''
#===================================================================================

def solution(tickets):
    routes = {} # 딕셔너리

    # 출발지를 키로, 도착지를 값으로 한다.
        # 단, 출발지가 동일할 경우를 대비해서 리스트에 도착지를 할당한다.
    for t in tickets:
        # 기존 딕셔너리에 해당 키가 없다면 우선적으로 리스트 생성 후, 값 할당
        routes[t[0]] = routes.get(t[0], []) + [t[1]]

    # 알파벳 순으로 도착지를 우선 선택
    # reverse를 해준 이유는, pop() 메소드로 값을 꺼내려고 하기 위함이다.
    for r in routes: # 키로 routes를 돈다.
        routes[r].sort(reverse=True)

    stack = ["ICN"] # 항상 "ICN"부터 시작하므로
    path = [] # 스택

    while len(stack) > 0: # 재귀 알고리즘으로 구현
        top = stack[-1] # 스택 최상위 원소 (즉, 출발지로 활용하고자 함)

        # 출발지(키)가 routes에 없거나, 있지만 이미 방문해서 없을 때
        if top not in routes or len(routes[top]) == 0:
            # 어차피, 이것들은 맨 나중에 방문하므로 stack에서 제거하고 path에 할당
            path.append(stack.pop())

        # 출발지(키)가 routes에 있거나, 있지만 아직 방문하지 않은 경우
        else:
            stack.append(routes[top][-1]) # 스택에 할당
            routes[top] = routes[top][:-1] # routes[top].pop()과 동일

    return path[::-1]

#===================================================================================

# 예제 1
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets)) # 	["ICN", "JFK", "HND", "IAD"]

# 예제 2
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets)) # 	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

# def solution(tickets):
#     answer = []
#     return answer