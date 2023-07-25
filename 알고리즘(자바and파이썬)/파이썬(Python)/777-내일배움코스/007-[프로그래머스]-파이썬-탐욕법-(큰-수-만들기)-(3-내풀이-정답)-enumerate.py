# [프로그래머스]-파이썬-탐욕법-(큰-수-만들기)-(3-내풀이-정답)-enumerate.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

*** 참고

'''
#===================================================================================

def solution(number, k):

    check = []

    for i, num in enumerate(number):

        while len(check) != 0 and check[-1] < number[i] and k > 0:
            # print("22222")
            check.pop()
            k = k-1

        if k == 0:
            check += list(number[i:])
            break

        check.append(number[i])

    # k가 남아 있을 경우
    check = check[:-k] if k > 0 else check

    return "".join(check)

#===================================================================================

# 예제 1
number = "1924"
k = 2
print(solution(number, k)) # "94"

# 예제 2
number = "1231234"
k = 3
print(solution(number, k)) # "3234"

# 예제 3
number = "4177252841"
k = 4
print(solution(number, k)) # "775841"

# def solution(number, k):
#     answer = ''
#     return answer