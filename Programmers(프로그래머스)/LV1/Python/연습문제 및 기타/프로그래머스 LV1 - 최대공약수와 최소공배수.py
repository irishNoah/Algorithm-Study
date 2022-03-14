# 프로그래머스 LV1 - 최대공약수와 최소공배수
# 분류 - 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12940

# 정확성 테스트의 케이스 16개 중 16개 성공
# 효율성 테스트는 없었음
# 총점 100.0

'''
해당 문제는 유클리드 호제법으로 접근하여 해결하였음
'''

def solution(n, m):
    answer = []

    # 최대공약수 구하기
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    # 최소공배수 구하기
    for i in range(max(n, m), (n*m)+1):
        if i % n == 0 and i % m ==- 0:
            answer.append(i)
            break

    return answer
    

n = 3
m = 12
print(solution(n, m))