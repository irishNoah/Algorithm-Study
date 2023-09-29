# [백준]1159-문자열-(농구-경기)-B2-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1159

'''
# 문제 풀이
>>> 해당 문제는 아스키코드 변환 함수인 chr()과 ord()를 물어보는 문제였다.


1. 사람 수(N) 입력
2. N에 맞는 문자열 이름 입력
- 입력할 때마다, 각 이름의 0번째 인덱스 값만 arr에 할당
3. flag 선언 >>> PREDAJA 판별
3. for문 활용
- count() 메소드 안에, chr()과 ord()를 사용해 각 알파벳이 몇 개 있는지 구함
>>> 만약, 5개 이상인게 있다면 바로 출력 / flag값 변환
>>> 만약, for문을 다 돌았는데도 없다면(즉, flag값이 변환 없다면) PREDAJA 출력

'''
#============================================================

import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    name = input()
    arr.append(name[0])

flag = False
for i in range(ord('a'), ord('z')+1):
    # print(ord('a')) # 97
    # print(ord('z')) # 122

    cnt = arr.count(chr(i))

    if cnt >= 5:
        flag = True
        print(chr(i), end="")

if flag == False:
    print("PREDAJA")