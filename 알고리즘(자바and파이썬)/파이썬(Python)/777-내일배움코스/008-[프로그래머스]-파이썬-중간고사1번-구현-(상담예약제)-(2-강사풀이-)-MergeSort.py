# [프로그래머스]-파이썬-중간고사1번-구현-(상담예약제)-(2-강사풀이-)-MergeSort.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
Merge Sort와 비슷한 느낌으로 구현해주시면 됩니다.
string의 시간을 적절히 숫자로 바꿔주는 작업이 필요합니다.
필수로 필요하진 않지만 예외처리를 줄이기 위해 booked/unbooked 끝에 dummy data를 추가하였습니다.

*** 참고

'''
#===================================================================================

def parse_time(t):
    h, m = map(int, t.split(':'))
    return 60 * h + m


def solution(booked, unbooked):
    # 예외처리를 줄이기 위해 booked/unbooked 끝에 dummy data를 추가
    # 더미코드를 추가해주지 않으면 return되는 answer의 길이가 1밖에 안됨
    booked = [(parse_time(t), name) for t, name in booked] + [(1000000, None)]
    unbooked = [(parse_time(t), name) for t, name in unbooked] + [(1000000, None)]

    # 문제에서는 애초에 정렬이 되어 있다고 나와 있지만, 문제 기준이 아닌
    # 실제 상황에서는 정렬이 되어 있지 않다고 가정하고 정렬 진행
    booked.sort()
    unbooked.sort()

    b, u, t, answer = 0, 0, 0, []

    # print("first booked = ", booked) # 예제1 기준 > [(550, 'lee'), (1000000, None)]
    # print("first unbooked = ", unbooked) # 예제1 기준 > [(540, 'kim'), (545, 'bae'), (1000000, None)]

    while b < len(booked) and u < len(unbooked):

        t1, t2 = booked[b][0], unbooked[u][0]

        if t1 <= t:
            answer.append(booked[b][1])
            b += 1
            t += 10
        elif t2 <= t:
            answer.append(unbooked[u][1])
            u += 1
            t += 10
        else:
            t = min(t1, t2)

    # print("before return anser = ", answer)

    answer.pop() # 더미 코드인 None을 pop()으로 제거
    return answer

#===================================================================================

# 예제 1
booked = [["09:10", "lee"]]
unbooked = [["09:00", "kim"],["09:05", "bae"]]
print(solution(booked, unbooked)) # ["kim", "lee", "bae"]

# 예제 2
booked = [["09:55", "hae"], ["10:05", "jee"]]
unbooked = [["10:04", "hee"],["14:07", "eom"]]
print(solution(booked, unbooked)) # ["hae", "jae", "hee", "eom"]

# def solution(booked, unbooked):
#     answer = []
#     return answer