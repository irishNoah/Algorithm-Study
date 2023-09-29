# [프로그래머스]-파이썬-연습문제-(가장-가까운-같은-글자)-LV1-(1-내풀이-정답)-다중인덱스활용(filter).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/142086

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)


*** 조건
>>> 1 ≤ s의 길이 ≤ 10,000
>>> s은 영어 소문자로만 이루어져 있습니다.

*** 설계 [총 4분 소요] / 총 풀이 시간[총 22분 소요]
> for문 활용
    - 만약, val과 s.index(문자) 값이 일치할 경우
        - -1을 할당한다.
    - 일치하지 않을 경우
        - filter 기법을 활용해 s[val] 이전까지의 문자열 중에서 s[val]와 동일한 문자를 가진
        다중 인덱스를 구한다.
            - 구해진 다중 인덱스 중에서 마지막 인덱스 값과 차를 구한 것을 할당한다.

*** 풀이 결과
> 정답은 맞추었지만, 몇몇 테스트 케이스에서 실행시간 값이 높은 것을 확인했다.
> 다른 사람이 푼 것을 보니 dict()를 활용해서 풀었고, 이것은 실행시간 값이 매우 짧게 걸렸다.

*** 참고
>>> 파이썬에서 리스트에서 원하는 값의 index를 여러개 찾는법
https://weejw.tistory.com/374



'''
#===================================================================================

def solution(s):
    answer = []

    for val in range(0, len(s)):
        if s.index(s[val]) == val:
            answer.append(-1)
        else:
            idx = list(filter(lambda e:s[e] == s[val], range(len(s[:val]))))

            answer.append(val-idx[-1])

    return answer

#===================================================================================

s = "banana"
print(solution(s)) # [-1, -1, -1, 2, 2, 2]

# def solution(s):
#     answer = []
#     return answer