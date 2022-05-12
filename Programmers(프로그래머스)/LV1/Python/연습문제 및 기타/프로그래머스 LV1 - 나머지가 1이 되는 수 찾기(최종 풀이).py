# 프로그래머스 LV1 - 나머지가 1이 되는 수 찾기(최종 풀이)
# 분류 - 월간 코드 챌리지 시즌 3
# https://programmers.co.kr/learn/courses/30/lessons/87389

# 정확성 테스트의 케이스 11개 중 11개 성공
# 효율성 테스트는 없었음
# 총점 100.0

"""
해당 문제는 '에라토스테스의 체' 방법을 활용해서 문제를 해결하였음
참고 링크 : https://lsh-story.tistory.com/57
"""

def solution(n):
    answer = 0 # 리턴할 값 answer

    # 에라토스테네스의 체 초기화 : n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n
    
    # n의 최대 약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if sieve[i] == True: # i가 소수인 경우
            for j in range(i+i, n, i): # i 이후 i 배수들을 False 판정
                sieve[j] = False

    # sieve를 통해 얻은 소수 목록을 seive_list에 대입
    # 참고로 seive 자체의 리스트 요소들을 True 또는 False로 이루어짐
    seive_list = [i for i in range(2, n) if sieve[i] == True]

    # seive_list 안에 있는 소수 요소들 중에서 문제가 요구하는 가장 작은 수 찾기
    # 가장 작은 수를 찾으면 for문을 종료함
    for value in seive_list:
        if n % value == 1:
            answer = value
            break

    return answer # answer 리턴

n = 12
print(solution(n)) # 출력 예 : 3