# [백준]1213-구현-(팰린드롬-만들기)-S3-(3-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1213

'''
*** 참고 URL
https://blockdmask.tistory.com/566

*** 시간 : 2초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건


*** 설계 [ 10분 소요] / 총 풀이 시간[총 27분 소요]
- counter를 활용해서 각 알파벳이 몇 개 있는지 구한다. > 딕셔러니(word)
- word에서 값이 홀수개인 것이 몇 개(cnt)인지 카운트한다.
    - 만약, cnt가 2개 이상이면 "I'm Sorry Hansoo" 를 출력하고 시스템을 종료한다.
        - 팰린드롬은 홀수 개인 알파벳이 2개 이상이면 안된다!!
    - cnt가 1이라면 mid에 해당 알파벳을 할당한다.
- word를 키를 기준 알파벳 순으로 정렬한다.
- 팰린드롬은 대칭이기 때문에
    - cnt가 0일 경우
        - for문을 돌며
            - answer += 알파벳 * (word[알파벳]//2)
        - for문 나온 이후
            - answer += answer[::-1]
    - cnt가 1일 경우
        - for문을 돌며
            - answer += 알파벳 * (word[알파벳]//2)
        - for문 나온 이후
            - answer += k + answer[::-1]

'''
#============================================================

import sys
import collections

val = sys.stdin.readline().rstrip() # AAABB

word = dict(collections.Counter(val))

cnt = 0 # 홀수가 몇 개인지 판별

mid = ""
for alpha, num in word.items():
    if num % 2 == 1:
        cnt += 1
        mid = alpha

if cnt >= 2:
    print("I'm Sorry Hansoo")
    sys.exit(0)


# 키를 기준으로 오름차순 정렬
# https://blockdmask.tistory.com/566
word = dict(sorted(word.items()))
# print(word)

answer = ""
for alpha, num in word.items():
    if num >= 2:
        answer += alpha * (num//2)

if mid != "":
    answer += mid + answer[::-1]
else:
    answer += answer[::-1]

print(answer)