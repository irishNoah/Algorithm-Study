# [프로그래머스]-파이썬-동적계획법-(N으로-표현)-(2-강사풀이-LV3)-아직내수준아냐.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]

*** 참고


'''
#===================================================================================

def solution(N, number):
    s = [set() for x in range(8)]

    for i, x in enumerate(s, start = 1):
        x.add(int(str(N) * i))

    for i in range(len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            answer = i+1
            break

        else:
            answer = -1

    return answer

#===================================================================================

# 예제 1
N = 5
number = 12
print(solution(N, number)) # 4

# 예제 2
N = 2
number = 11
print(solution(N, number)) # 3

# def solution(N, number):
#     answer = 0
#     return answer