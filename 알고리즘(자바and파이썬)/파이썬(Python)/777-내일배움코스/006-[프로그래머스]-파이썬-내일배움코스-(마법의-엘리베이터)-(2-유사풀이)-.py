# [프로그래머스]-파이썬-내일배움코스-(마법의-엘리베이터)-(2-유사풀이)-.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/148653

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

*** 유사 풀이
> 참고 : https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Programmers-%EB%A7%88%EB%B2%95%EC%9D%98-%EC%97%98%EB%A6%AC%EB%B2%A0%EC%9D%B4%ED%84%B0-Python
> 나는 rock에 무조건 0~5는 더해주고,
그 외의 수는 (10-int(storey[x])+1) 를 더하여 계산했다.
-----------------------------------------------------------------------------------------------
> 하지만, 가운데 수 5는 조심해서 생각해야 한다.
> 다음 자리수가 5~9에 해당하는지와, 0~4에 해당하는지까지 고려해야 한다.

즉, 이를 기준으로 설계하면 아래와 같다.

1) 만약 현재 자릿값이 6 ~ 9 에 해당한다면 10 에 도달하는 방향으로 마법의 돌을 사용한다.
2) 만약 현재 자릿값이 0 ~ 4 에 해당한다면 0 에 도달하는 방향으로 마법의 돌을 사용한다.
3)만약 현재 자릿값이 5 에 해당한다면 다음 자릿값에 따라 이동하는 방향을 정할 수 있다.
    3-1. 만약 다음 자릿값이 5 ~ 9에 해당한다면 현재 자릿값을 10 에 도달하는 방향으로 마법의 돌을 사용한다.
    3-2. 만약 다음 자릿값이 0 ~ 4에 해당한다면 현재 자릿값을 0 에 도달하는 방향으로 마법의 돌을 사용한다.

'''
#===================================================================================


def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10

    return answer


#===================================================================================

# 예제 1
storey = 16
print(solution(storey)) # 6

# 예제 2
storey = 2554
print(solution(storey)) # 16

# def solution(storey):
#     answer = 0
#     return answer