# 프로그래머스 LV2 - 소수 찾기(두 번째 풀이)
# 분류 - 완전탐색
# https://programmers.co.kr/learn/courses/30/lessons/42839

# 정확성 테스트의 케이스 12개 중 12개 성공
# 효율성 테스트는 없었음
# 총점 100.0

'''
초기 풀이 때에 1시간이나 투자를 했는데 해결이 안되서
다른 분께서 푸신 코드를 참고해서 풀었다.
다른 분께서 푸신 코드의 전체적인 느낌은 내가 짠 코드와 비슷한데,
다른 점이라면 난 for문과 if문을 많이 써서 했단 점이다.
'''

'''
풀이 과정

1) check라는 함수를 만들어서 소수를 판정
여기서, math.sqrt를 사용하는 이유는 제곱수의 경우 소수가 아니기 때문에 이를 통해 판정
2) permutations를 이용해서 모든 경우의 수를 만들고 판정
단, 여기서 중복되는 수가 발생해서 set으로 미리 줄이고 하면 속도가 많이 빨라짐
3) answer에 모든 소수를 집어넣고 길이를 출력하면 정답
'''

from itertools import permutations
import math

def check(n):
    k = math.sqrt(n)

    if n < 2: 
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(perlist)):
            if check(int(i)):
                answer.append(int(i))

    answer = len(set(answer))

    return answer

numbers = "17"

print(solution(numbers)) # 결과 예 : 3