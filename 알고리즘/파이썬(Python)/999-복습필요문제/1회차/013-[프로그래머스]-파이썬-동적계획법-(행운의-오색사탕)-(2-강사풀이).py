# [프로그래머스]-파이썬-동적계획법-(행운의-오색사탕)-(2-강사풀이).py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- cache에 얼마나 첫번째부터 일치하는지에 대한 정보를 저장하는 것을 목표로 합니다.
- 계속 일치하면 쭉 이어나가고 아닌 경우, 일치하는 구간이 나올때까지 cache를 타고 계속 뒤로 갑니다.
- ache가 완성되면 각 position에 대해 cache를 얼마만큼 탈 수 있느냐가 곧 정답이 됩니다.

*** 참고

'''
#===================================================================================

def solution(candy, positions):
    # part1
    n_match, cache = 0, [0] * len(candy)
    for i in range(1, len(candy)):
        while n_match and candy[n_match] != candy[i]:
            n_match = cache[n_match]
        if candy[n_match] == candy[i]:
            n_match += 1
            cache[i] = n_match

    # part2
    answer = []
    for pos in positions:
        ans = 0
        while cache[pos - 1]:
            pos = cache[pos - 1]
            ans += 1
        answer.append(ans)

    return answer

#===================================================================================

# 예제 1
candy = "RYRYRGPRYRYRBB"
positions = [12,1,14,7]
print(solution(candy, positions)) # [3,0,0,0]

# 예제 2
candy = "BPBRBPBRB"
positions = [3, 6, 9]
print(solution(candy, positions)) # [1,1,2]


# def solution(candy, positions):
#     answer = []
#     return answer