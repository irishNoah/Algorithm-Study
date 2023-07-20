# [프로그래머스]-파이썬-내일배움코스-(가장-큰-수)-(1-내풀이-실패)-7점.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

*** 참고

'''
#===================================================================================

def solution(numbers):
    answer = ""

    # 문자열 리스트로 변환 and 정렬까지
    numbers = sorted(list(map(str, numbers)))
    numbers.append("1")
    # print(numbers)

    # 앞 자리가 동일한 것에서 문제가 되는 것 swap
    # 예 : 3과 34는 swap X / 3과 32는 swap / 3과 331은 swap
    # 예 : 34와 323은 swap / 34와 347은 swap x
    # => 즉, 맨 앞자리가 3일 경우, 아무리 인간 세상에서 더 큰 수라도
    # 각 자리가, 3보다 작다면 swap을 해줘야 한다.
    for idx in range(len(numbers)-1):
        if numbers[idx][0] == numbers[idx+1][0]: # 즉, 맨 첫자리가 같을 때
            for x in range(len(numbers[idx+1])):
                if numbers[idx+1][x] < numbers[idx]:
                    numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
                    break

    rev_numbers = list(reversed(numbers))
    for idx in range(1, len(numbers)):
        answer += rev_numbers[idx]

    return answer


#===================================================================================

# 예제 1
numbers = [6, 10, 2]
# numbers = sorted(list(map(str, numbers)))
# print(numbers)
print(solution(numbers)) # "6210"

# 예제 2
numbers = [3, 30, 34, 5, 9]
# numbers = sorted(list(map(str, numbers)))
# print(numbers)
print(solution(numbers)) # 954330

# def solution(numbers):
#     answer = ''
#     return answer