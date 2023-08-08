# [프로그래머스]-파이썬-DFS+BFS-(여행경로)-LV3-(1-내풀이-실패)-50점-딕셔너리.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 20분 소요] / 총 풀이 시간[총 63분 소요]

*** 참고
> 딕셔너리의 값을 리스트로 넣고 싶다면, 먼저 list()로 해줘야 한다.
- 그냥, append()를 통해 넣어주면 에러 난다!!!

> 특정 키에 대한 값이 여러개인데, 이 값중 하나는 어떻게 없앨까?
- pop()메소드로 없앤다!
- {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']} 에서
- move['ICN'].pop()울 하면???
    - {'ICN': ['SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']} 이 된다!

*** 틀린 이유 분석
>>> 그래도 LV3 문제에서 50점 맞은 것은 잘했어!

1) [a, b] 즉 출발지 a와 b가 중복될 수 있다는 것을 간과 했다.
예를 들어, ["ICN", "SFO"]이 여러 번 들어가 있을 수 있다는 것이다.
> 즉, 내가 푼 방식처럼 딕셔너리를 사용하면 안된다는 것이다!

2) 만약,
tickets = [["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]
일 경우에는

결과가 ["ICN", "CCC", "DDD", "ICN", "AAA", "BBB", "AAA", "BBB"] 이어야 한다.

뮨제에서는 가능한 경로에서는 알파벳으로 앞에 있는 도착지 먼저 방문한다고 했지만,
모든 도시를 방문할 수 없는 경우는 없다고 나와 있다.

만약, 사전순으로 ICN 다음에 AAA를 방문했다면, 모든 도시를 탐방할 수 없다.
즉, 재귀 호출을 이용한 백트래킹 기법으로 풀었어야 한다는 것이다.

*** 다음에는
1) 중복 여부가 가능한지 안한지 체크하기
2) 규칙은 따르되 예외는 없는지 체크하기


'''
#===================================================================================

def solution(tickets):
    # print("=" * 50)
    answer = ['ICN']

    # 다중 정렬 진행 > 차례대로 넣어주고, pop을 통해서 뒤에서부터 가져오기 위해
    tickets = sorted(tickets, key=lambda x:(x[1]), reverse=True) # 목적지 b는 내림차순 정렬
    tickets = sorted(tickets, key=lambda x:(x[0])) # 목적지 a는 오름차순 정렬
    # print("tickets = ", tickets)

    # 딕셔너리 a(출발지) > 키 /// b(도착지) > 값
    move = dict()
    for idx in range(len(tickets)):
        a, b = tickets[idx][0], tickets[idx][1]

        if move.get(a) == None:
            move[a] = list()
            move[a].append(b)
        else:
            move[a].append(b)

    # print("move = ", move)

    # 다음 행선지를 알파벳 순으로 차례대로 구함
    for idx in range(len(tickets)):
        val = move[answer[-1]].pop()
        answer.append(val)

    return answer

#===================================================================================

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# move = dict()
#
# for idx in range(len(tickets)):
#     a, b = tickets[idx][0], tickets[idx][1]
#     print(a, b)
#
#     if move.get(a) == None:
#         move[a] = list()
#         move[a].append(b)
#     else:
#         move[a].append(b)
#
# print(move)
# print(len(move['ICN']))
# move['ICN'].pop()
# move['ICN'].pop()
# print(move)

# 예제 1
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets)) # 	["ICN", "JFK", "HND", "IAD"]

# 예제 2
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets)) # 	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

# def solution(tickets):
#     answer = []
#     return answer