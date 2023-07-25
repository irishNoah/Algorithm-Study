# [프로그래머스]-파이썬-정렬-(가장-큰-수)-(3-내풀이-정답)-다중정렬.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

*** 참고

'''
#===================================================================================

def solution(numbers):

    numbers = list(map(str, numbers))
    answer = sorted(numbers, key = lambda x : (x*4)[:4], reverse=True)

    # numbers의 원소들이 0으로만 이루어져 있을 경우 0이 몇 개이든 답은 0이어야 하므로
    if answer[0] == "0":
        return "0"
    else:
        return "".join(answer)

#===================================================================================

# 예제 1
numbers = [6, 10, 2]
# print(numbers)
print(solution(numbers)) # "6210"

# 예제 2
numbers = [3, 30, 34, 5, 9]
# print(numbers)
print(solution(numbers)) # "954330"

# 예제 3
numbers = [0,0,0]
# print(numbers)
print(solution(numbers)) # "0"

# def solution(numbers):
#     answer = ''
#     return answer