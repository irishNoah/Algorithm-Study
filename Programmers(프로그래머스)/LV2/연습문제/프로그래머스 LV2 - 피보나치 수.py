# 프로그래머스 LV2 - 피보나치 수
# https://programmers.co.kr/learn/courses/30/lessons/12945

# 정확성 테스트의 케이스 14개 중 14개 성공
# 효율성 테스트는 없었음
# 총점 100.0점


def solution(n):
    answer = 0

    '''
    F(0) = 0, F(1) = 1 이므로 F(0)과 F(1) 값을
    리스트 val에 삽입
    '''
    val = [0, 1]
    
    # 2부터 n까지 동적 계획법을 이용하여 f(n) 값 구하기
    for i in range(2, n+1):
        val.append(val[i-1] + val[i-2])

    answer = (val[-1]) % 1234567
    return answer

n = 5
print(solution(n))