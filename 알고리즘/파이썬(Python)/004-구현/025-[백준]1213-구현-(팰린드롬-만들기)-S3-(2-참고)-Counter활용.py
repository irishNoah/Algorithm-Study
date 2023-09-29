# [백준]1213-구현-(팰린드롬-만들기)-S3-(2-참고)-Counter활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1213

'''
*** 참고 URL
https://star7sss.tistory.com/391

*** 시간 : 2초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건


*** 설계 [총 13분 소요] / 총 풀이 시간[총 50분 소요]
1. dict 형태로 현재 알파벳이 뭐가 있는지, 몇개인지를 넣는다. -> Counter 이용
2. 입력값의 알파벳 수를 구해서 홀수가 2개 이상인지 파악해야 한다. -> Counter.items() 이용
3. 홀수가 1개라면, 현재 홀수의 알파벳을 저장해준다. -> 나중에 붙여주기 위함.
4. 입력받은 값을 정렬한 후, FOR문을 통해 가지고 있는 알파벳을 result에 넣는다.
5. 이때, 입력받은 값의 길이의 몫을 구해 현재 알파벳에 곱해준다.
6. 마지막에 홀수 알파벳과, 역순으로 바꾼 앞 리스트를 붙여준다.

*** 틀린 이유

'''
#============================================================

import collections
import sys

word = sys.stdin.readline().rstrip()
check_word = collections.Counter(word)
cnt = 0
result = ''
mid = ''
for k, v in list(check_word.items()):
    if v % 2 == 1: #홀수라면
        cnt += 1
        mid = k #중간에 들어갈 값으로 저장
        if cnt >= 2: #홀수가 2개이상이면 팰린드롬이 될 수 없다!!
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(check_word.items()): #정렬을 통해 사전순으로 for문을 돌게함
    result += (k * (v // 2)) #정확히 절반으로 나뉜 문자열을 만들어야 하므로 현재 갯수를 2로 나눠줌
print(result + mid + result[::-1]) # 앞+중간+뒤 를 더해 문자열 출력