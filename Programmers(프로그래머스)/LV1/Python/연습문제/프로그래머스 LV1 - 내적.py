# 프로그래머스 LV1 - 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128?language=python3

# 정확성 테스트의 케이스 9개 중 9개 성공
# 효율성 테스트는 없었음
# 총점 100.0점

def solution(a, b):
    # 리턴할 값 answer
    answer = 0 

    '''
    zip을 이용하여 a와 b의 각 n번째 요소를 곱한 값을 
    anwer에 합산하기
    '''
    for val_1, val_2 in zip(a, b):
        answer += (val_1 * val_2)

    # answer 리턴하기
    return answer

a = [-1,0,1]	
b = [1,0,-1]
print(solution(a,b))