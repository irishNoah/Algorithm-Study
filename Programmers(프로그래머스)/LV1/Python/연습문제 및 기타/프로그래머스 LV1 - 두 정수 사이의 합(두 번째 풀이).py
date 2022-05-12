# 프로그래머스 LV1 - 두 정수 사이의 합(두 번째 풀이)
# 분류 - 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12912

# 정확성 테스트의 케이스 16개 중 16개 성공
# 효율성 테스트는 없었음
# 총점 100.0

'''
해당 풀이로 시간 복잡도를 비약적으로 줄였음
만약 1~6까지의 범위라 할 때
1 2 3 4 5 6이 있고
1+6, 2+5, 3+4의 값이 모두 동일하므로
맨 앞의 숫자와 맨 뒤의 수를 합산하고, 전체 수가 6개 일때의 절반인 3을 곱하면
7 * 3 = 21이 된다.

만약 1~7의 범위라고 하면
1 2 3 4 5 6 7 이 있고
1+7, 2+6, 3+5의 값은 모두 같고 가운데 수 4만 남으므로
가운데의 수를 제외한 값은 위의 설계와 동일하며 마지막에 가운데 수만 더해주면 된다.
'''


def solution(a, b):
    answer = 0


    if a == b:
        answer = a
        return answer

    if b < a :
        x = a
        a = b
        b = x

    a_b_len = b - a + 1

    if a_b_len % 2 == 0 :
        answer = (a+b) * (a_b_len//2)

    else :
        answer = (a+b) * ((a_b_len-1)//2) + ((a+b)/2)

    return int(answer)

a = 5
b = 3
print (solution(a, b))