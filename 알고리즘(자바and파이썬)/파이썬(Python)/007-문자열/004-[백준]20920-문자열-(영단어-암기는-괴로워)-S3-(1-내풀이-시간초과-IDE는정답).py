# [백준]20920-문자열-(영단어-암기는-괴로워)-S3-(1-내풀이-시간초과-IDE는정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/20920

'''
##### 문제 풀이

# 핵심
* 단어 길이가 M 이상인 단어들만 외운다.

단어장 우선순위
1. 자주 나오는 단어일수록 앞에 배치한다.
2. 해당 단어의 길이가 길수록 앞에 배치한다.
3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

# 설계
> M{단어 개수(10만)}과 M(단어의 길이) 공백 입력

> for문 활용해서 N개 입력
- 입력과 동시에 단어의 길이 M보다 작으면 pass
>>  M 미만일 경우 pass
- M 이상일 경우
>>> 만약, 리스트에 없는 단어라면?
- 2차원 리스트에 단어 / 단어의 길이 / 사용빈도수 값(cnt) 1 할당
>>> 만약, 리스트에 있는 단어라면?
- 2차원 리스트에 있는 단어의 사용빈도수 값(cnt) 1 증가

> for문 끝나고 나서
- 다중 리스트 정렬을 한다. (단어장 우선순위 대로)

> 리스트 컴프리핸션을 통해 차례대로 출력한다.

'''
#============================================================

import sys

# N : 단어의 개수 / M : 단어장에 들어갈 수 있는 단어의 최소 길이
N, M = map(int, sys.stdin.readline().split())

book = []
for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if len(word) < M:
        continue

    else:
        if len(book) == 0:
            # 단어, 단어의 길이, 단어 반복 횟수
            book.append([word, len(word), 1])
            continue

        # 입력 받은 단어가 리스트에 이미 있나 확인
        flag = False; check = 0
        for i in range(len(book)):
            if book[i][0] == word:
                flag = True
                check = i
                break

        # 없으면
        if flag == False:
            # 단어, 단어의 길이, 단어 반복 횟수
            book.append([word, len(word), 1])

        # 있으면
        elif flag == True:
            # 단어 반복 횟수 1 증가
            book[check][2] += 1

res = sorted(book, key=lambda x:(-x[2],-x[1],x[0]))
for i in range(len(res)):
    print(res[i][0])



