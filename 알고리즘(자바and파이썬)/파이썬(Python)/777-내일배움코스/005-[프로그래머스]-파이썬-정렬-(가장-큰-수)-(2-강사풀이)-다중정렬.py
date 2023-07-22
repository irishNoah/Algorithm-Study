# [프로그래머스]-파이썬-정렬-(가장-큰-수)-(2-강사풀이)-다중정렬.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]
>>> 내꺼의 최종 시간 복잡도는 O(N^2) 이다.
- 강사도, 첫 번째 설계 때 일반적으로 생각했을 때는 O(N^2) 이라고 했지만,
성능 상 이것은 좋지 않다고 언급 >>> 즉, IDE 상으로는 맞게 잘했어!

>>> 애초에 이것은 정렬을 활용해야 하기 때문에, O(N*logN)의 복잡도를
기본적으로 소유하고 있음
- 그럼, 다중 정렬으로 해결할 수 있는 방안이 없을까? 라는 생각을 해봐야지!



*** 참고

'''
#===================================================================================

def solution(numbers):

    numbers = [str(x) for x in numbers]

    '''
    # 예제 2의 3, 30, 34와 같은 경우 정렬이 30, 3, 34와 같이 되어야 한다.
    # numbers의 최대 자리수가 1000의 자리까지이니까 x를 4번 곱한 후 [:4]를 해주면
    # 3 > 3333 / 30 > 3030 / 34 > 3434 와 같이 되어, 이를 기준으로 정렬해주면
    # 원하는 대로 30, 3, 34와 같이 된다.
    '''
    numbers.sort(key = lambda x : (x*4)[:4], reverse=True)

    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)

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