# [백준]-파이썬-딕셔너리-(팰린드롬-만들기)-(1-내풀이-정답)-100점-힙.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1213

'''
*** 제한 > 시간 : 2초 (기본 1초) / 메모리 : 128MB (기본 128MB)
*** 조건
*** 설계 [총 3분 소요] / 총 풀이 시간[총 -분 소요]
*** 참고

'''
#===================================================================================

'''
1. 입력 / 문자열 to list / list 오름차순 정렬
2. Counter로 각 알파벳 갯수 구함
3. 다 구했을 때 홀수 갯수를 가진 알파벳의 수가 1개보다 많으면?
- 팰린드롬이 될 수 없다.
4. 1개 이하라면
> 팰린드롬이 될 수 있다.
> 만약, 홀수 알파벳이 있다면
- 이 알파벳을 cmp에 둔다. (처음에는 cmp = "" 로 초기화 할 것)
5. answer라고 하는 변수에 counter에 있는 각 알파벳 갯수의 절반씩을 더한다.
- 그리고 answer += cmp
6. answer += answer[::-1] >>> 역순
 
'''

import sys
import collections
input = sys.stdin.readline

word = sorted(list(input().rstrip()))

book = dict()

for alp in word: # 사전 구성하기
    if alp not in book:
        book[alp] = 1
    else:
        book[alp] += 1

cmp = ""
cnt = 0 # 알파벳 갯수가 홀수인 것이 몇 개인지 파악하는 변수
for k, v in book.items(): # 홀수 갯수 파악
    if v % 2 == 1:
        cnt += 1
        cmp = k

    if cnt > 1:
        print("I'm Sorry Hansoo")
        sys.exit()

# 팰린드롬 문자 구하기
answer = ""
for k, v in book.items():
    answer += k * (v // 2)

save = answer
answer += cmp
answer += save[::-1]
print(answer)

#===================================================================================