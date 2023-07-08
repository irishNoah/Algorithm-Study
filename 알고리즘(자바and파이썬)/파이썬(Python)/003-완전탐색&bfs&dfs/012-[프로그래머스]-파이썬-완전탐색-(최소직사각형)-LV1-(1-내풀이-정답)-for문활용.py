# [프로그래머스]-파이썬-완전탐색-(최소직사각형)-LV1-(1-내풀이-정답)-for문활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)


*** 조건
sizes의 길이는 1 이상 10,000 이하입니다.
sizes의 원소는 [w, h] 형식입니다.
w는 명함의 가로 길이를 나타냅니다.
h는 명함의 세로 길이를 나타냅니다.
w와 h는 1 이상 1,000 이하인 자연수입니다.

*** 설계 [총 16분 소요] / 총 풀이 시간[총 33분 소요]
- 주어진 가로와 세로 중에서 최대값 (가로 및 세로)룰 찾는다.
# max(세로)가 더 크거나 같을 경우 >>> 예재2 참고
> 각 abs(max(세로)-arr[i][0]) <= abs(max(세로)-arr[i][1])을 경우
- swap
- 바뀐 가로값을 기준으로 새로운 최대 가로값을 찾는다.

# max(가로)가 더 클 경우
> 각 abs(max(가로)-arr[i][1]) <= abs(max(가로)-arr[i][0])을 경우  >>> 예제1 참고
- swap
- 바뀐 새로값을 기준으로 새로운 최대 세로값을 찾는다.

'''
#===================================================================================

def solution(sizes):
    answer = 0

    maxGaro = 0; maxSero = 0
    for i in range(len(sizes)):
        if sizes[i][0] > maxGaro:
            maxGaro = sizes[i][0]
        if sizes[i][1] > maxSero:
            maxSero = sizes[i][1]

    if maxSero >= maxGaro:
        newMaxGaro = 0

        for i in range(len(sizes)):
            if abs(maxSero-sizes[i][0]) <= abs(maxSero-sizes[i][1]):
                sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

            # 이것의 위치가 중요!!!
            # 위 if문 내부에 있으면 안됨!!!
            if sizes[i][0] > newMaxGaro:
                newMaxGaro = sizes[i][0]

        answer = maxSero * newMaxGaro

    else:
        newMaxSero = 0

        for i in range(len(sizes)):
            if abs(maxGaro-sizes[i][1]) <= abs(maxGaro-sizes[i][0]):
                sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

            # 이것의 위치가 중요!!!
            # 위 if문 내부에 있으면 안됨!!!
            if sizes[i][1] > newMaxSero:
                newMaxSero = sizes[i][1]

        answer = maxGaro * newMaxSero

    return answer

# #############################################################

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))