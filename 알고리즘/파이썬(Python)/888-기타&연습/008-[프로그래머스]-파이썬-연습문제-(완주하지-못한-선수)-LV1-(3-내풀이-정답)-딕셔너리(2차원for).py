# [프로그래머스]-파이썬-연습문제-(완주하지-못한-선수)-LV1-(3-내풀이-정답)-딕셔너리(2차원for).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/142086

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 10분 소요] / 총 풀이 시간[총 28분 소요]
>>>>> 해시로 풀자!
>>> 구체적 설명은 코드 주석에 첨부
- 내가 이번에 짠 거는 잘 짜긴 했지만 2중 for문이기 때문에 o(n^2)의 시간복잡도를 가진다.
- 참고했던 것은 1중 for문으로 했는데 in과 not in을 활용해서 사용했다.
    - 딕셔너리[알파벳] = 문자열 s의 인덱스 위치
- 그래도 1번째로 풀었었을 때는 filter()로 풀어서 문제를 맞추기는 높았어도
테스트케이스에서 시간 가장 높은게 7589ms나 될 정도로 오지게 높았지만
이번에 3번째로 내가 푼 걸로는 가장 높은게 18ms로 낮추었다. >>> 잘한 것 같다.

'''
#===================================================================================

def solution(s):
    answer = []

    s = list(s)
    check = dict()

    for val in s: # s의 원소를 key 값으로 사용한다.

        for key in check: # 기존에 있던 것들을 한 칸씩 증가하게 한다.
            check[key] += 1

        # None을 확일할 때는
        # check.get(val) == None 으로 해야지
        # check[val] == None으로 하면 큰일난다!
        if check.get(val) == None:
            answer.append(-1)
            check[val] = 0

        else:
            answer.append(check[val])
            check[val] = 0

    return answer

#===================================================================================

# 예제 1
s = "banana"
print(solution(s)) # "[-1,-1,-1,2,2,2]"

# 예제 2
s = "foobar"
print(solution(s)) # "[-1,-1,1,-1,-1,-1]"

# def solution(s):
#     answer = []
#     return answer