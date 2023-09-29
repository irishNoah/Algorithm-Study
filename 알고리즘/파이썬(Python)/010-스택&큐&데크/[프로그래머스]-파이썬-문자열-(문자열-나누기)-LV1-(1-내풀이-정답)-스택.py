# [프로그래머스]-파이썬-문자열-(문자열-나누기)-LV1-(1-내풀이-정답)-스택.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/140108

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건(제한사항)
1 ≤ s의 길이 ≤ 10,000
s는 영어 소문자로만 이루어져 있습니다.

*** 정확성 테스트
- 100점

*** 설계 [총 12분 소요] / 총 풀이 시간[총 20분 소요]
- s의 길이가 10000이므로 최대 O(N^2) 이하의 시간복잡도로 문제를 구성
- 우선, s를 역순으로 만든다. s = s[::-1]
- 단어 개수에 대한 변수 > answer
- 스택을 이용한다. -> 스택 변수 stack
- same = 0 / differ = 0
- while > s의 길이가 0이 아닐 때까지
    - 만약 stack이 비어있다?
        - cmp(맨 처음 문자, 지문에 따지면 x의 역할) = s[-1]
    - 만약, s의 마지막 요소와(s[-1]) cmp가 같다면?
        - stack.append(s.pop()) ### 스택에 s의 마지막 요소 할당
        - same += 1
    - 만약, s의 마지막 요소와(s[-1]) cmp가 다르다면?
        - stack.append(s.pop()) ### 스택에 s의 마지막 요소 할당
        - differ += 1
    - 만약, same과 differ의 갯수가 동일하다면?
        - stack 비우기 >>> stack.clear()
        - same과 differ 초기화
            - same = 0 / differ = 0
        - answer += 1
    - 만약, s의 길이가 0이 됐는데, same과 differ의 길이가 다르다면?
        - answer += 1
    
'''
# #############################################################
def solution(s):
    
    s = s[::-1]
    s = list(map(str,s))
    # print(s)
    
    answer = 0 # 단어 갯수
    stack = [] # 스택
    same = 0 # 기준 문자와 동일한 알파벳 갯수
    differ = 0 # 기준 문자와 다른 알파벳 갯수
    
    while len(s) > 0:
        # stack이 비어있을 때는 기준 문자 정하기 (지문에서의 x)
        if len(stack) == 0:
            cmp = s[-1]
        
        # 기준 문자와 동일한 문자와 다른 문자의 갯수 파악
        if cmp == s[-1]:
            stack.append(s.pop())
            same += 1
        elif cmp != s[-1]:
            stack.append(s.pop())
            differ += 1
        
        # 동일한 문자와 다른 문자의 갯수 동일한 경우
        # > 스택 초기화, 동일 및 다른 변수 초기화, 단어 갯수 증가
        if same == differ:
            stack.clear()
            same = 0; differ = 0
            answer += 1
        
        # pop()으로 인해 s의 길이가 0이 됐는데, stack에 남은 게 있다면
        # > 단어 갯수 증가
        if len(s) == 0:
            if len(stack) != 0:
                answer += 1
            break
    
    return answer