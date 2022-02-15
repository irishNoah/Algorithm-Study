# 프로그래머스 LV2 - 가장 큰 수(초기풀이)
# https://programmers.co.kr/learn/courses/30/lessons/42746

# 정확성 테스트의 케이스 15개 중 15개 성공
# 효율성 테스트는 없었음
# 총점 100.0점

def solution(numbers):
    answer = '' # 리턴할 문자열 answer

    '''
    처음 주어진 리스트는 정수형 리스트이다.
    사전 형식으로 내림차순 정렬 후 문제를 해결하기 위한 사전 작업으로 
    numbers의 요소들을 str 타입으로 변환한다.
    '''
    str_numbers = [str(num) for num in numbers]

    '''
    숫자는 1000 이하의 숫자이므로  곱하기 3한 값으로 비교.
    우선 사전값으로만 정렬하면[9,5,34,30,3]과 같이 정렬됨.
    그러나 문제 결과 예시를 보면 3이 30보다 앞으로 와야 함.
    이렇게 해주기 위해 숫자는 1000 이하의 숫자라는 조건을 이용하여
    최대값을 생각해 3을 곱해주어야 하며 곱할 시 [999, 555, 343434, 303030, 333]이 됨.
    이것을 정렬하면 [999, 555, 343434, 333, 303030]이 됨.
    이렇게 되야 원하는 데로 정렬이 될 수 있음
    '''
    str_numbers.sort(key=lambda num: num*3, reverse=True)


    '''
    리턴할 answer은 정수형으로 리턴해주어야 하므로
    반환할 때 int로 변환해준 후 다시 str로 변경
    '''
    answer = str(int("".join(str_numbers)))

    return answer

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))