# [프로그래머스]-파이썬-스택-(과일-장수)-LV1-(1-내풀이-정답)-스택활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/135808

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건(제한사항)
>>> 3 ≤ k ≤ 9
>>> 3 ≤ m ≤ 10
>>> 7 ≤ score의 길이 ≤ 1,000,000
>>> 1 ≤ score[i] ≤ k
>>> 이익이 발생하지 않는 경우에는 0을 return 해주세요.

*** 설계 [총 5분 소요] / 총 풀이 시간[총 18분 소요]
- score의 길이가 1000000(백만)이므로 시간 복잡도는 최대 O(N * logN) 이하로 구성한다.
- score을 오름차순으로 정렬하여 스택구조로 만든다.
- score의 최상위 요소(맨 마지막 요소)를 pop하여 스택 리스트인 stack에 할당한다.
    - stack의 길이가 m이 되면 >>> stack의 맨 마지막 값(최저 사과 점수) * m * 1로 한다. => answer 변수에 이 점수를 더한다.
        - 의문 >>>> 굳이 동일한 박스 2개이면, 2개를 곱한 경우 곱해줘야 하나? => 어차피 1+1 구성으로 해도 되잖아
    - 만약, score의 길이가 0이 됐는데, stack의 길이가 m이 안되면
        - break
- 어차피, answer이 0이 되면 그냥 이익이 발생하지 않는 구조

*** 정확성 테스트
- 100점
'''
# #############################################################
def solution(k, m, score):
    
    stack = []
    score.sort() # 스택 활용하기 위한 오름차순 정렬
    
    answer = 0 # 최대 이익
    while True:
        if len(stack) == m:
            answer += stack[-1] * m * 1
            stack.clear() # 스택 비워버리기
            
        if len(score) == 0: # while문 종료 조건
            break
        
        stack.append(score.pop())
        
        
    return answer